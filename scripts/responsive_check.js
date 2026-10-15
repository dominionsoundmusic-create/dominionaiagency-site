// Responsive QA (Playwright + the preinstalled Chromium): serves dist/ locally, then for every page at 390, 768,
// 1024, 1440 and 1920 wide checks horizontal overflow (without hiding it) and rows that leave a hole on the right
// (a card / grid / step / price / fact row whose last line is shorter and not centered), and broken images.
// Screenshots: node scripts/responsive_check.js --shots / /ai-receptionist/ ... (1440, 1920, 2560 full page, after
// scrolling so lazy images load) into the scratch folder given by SHOTS_DIR (default ./shots).
// Usage: node scripts/responsive_check.js [--only /path/] [--shots url...]
const { chromium } = require(process.env.PW || 'playwright');
const http = require('http'); const fs = require('fs'); const path = require('path');
const DIST = path.join(__dirname, '..', 'dist');
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.png': 'image/png', '.woff2': 'font/woff2', '.ico': 'image/x-icon' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p.endsWith('/')) p += 'index.html';
  let f = path.join(DIST, p);
  if (!fs.existsSync(f) && fs.existsSync(f + '.html')) f += '.html';
  if (!fs.existsSync(f)) { res.writeHead(404); res.end(fs.readFileSync(path.join(DIST, '404.html'))); return; }
  res.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' });
  res.end(fs.readFileSync(f));
});
function pages() {
  const out = [];
  (function walk(d) { for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const f = path.join(d, e.name);
    if (e.isDirectory()) walk(f); else if (e.name.endsWith('.html')) {
      let u = '/' + path.relative(DIST, f).split(path.sep).join('/');
      if (u.endsWith('/index.html')) u = u.slice(0, -10);
      if (u === '/index.html') u = '/';
      out.push(u);
    } } })(DIST);
  return out.sort();
}
(async () => {
  const args = process.argv.slice(2);
  const only = args.includes('--only') ? args[args.indexOf('--only') + 1] : '';
  const shots = args.includes('--shots') ? args.slice(args.indexOf('--shots') + 1) : null;
  await new Promise(r => server.listen(8765, r));
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch());
  const base = 'http://localhost:8765';
  let problems = 0;
  if (shots) {
    const dir = process.env.SHOTS_DIR || 'shots'; fs.mkdirSync(dir, { recursive: true });
    for (const u of shots) for (const w of [1440, 1920, 2560]) {
      const pg = await browser.newPage({ viewport: { width: w, height: 1000 } });
      await pg.goto(base + u, { waitUntil: 'load' });
      await pg.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 250)); } window.scrollTo(0, 0); });
      await pg.waitForTimeout(1500);
      const name = (u === '/' ? 'home' : u.replace(/[\/.]+/g, '-').replace(/^-|-$/g, '')) + '-' + w + '.png';
      await pg.screenshot({ path: path.join(dir, name), fullPage: true });
      await pg.close();
    }
  } else {
    for (const u of pages().filter(u => !only || u === only)) {
      for (const w of [390, 768, 1024, 1440, 1920]) {
        const pg = await browser.newPage({ viewport: { width: w, height: 900 } });
        await pg.goto(base + u, { waitUntil: 'load' });
        await pg.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 800) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 20)); } });
        await pg.waitForTimeout(150);
        const r = await pg.evaluate(() => {
          const issues = [];
          const sw = document.documentElement.scrollWidth, cw = document.documentElement.clientWidth;
          if (sw > cw + 1) {
            const wide = [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > cw + 1).slice(0, 3).map(e => e.tagName + '.' + e.className);
            issues.push(`overflow ${sw}>${cw}: ${wide.join(', ')}`);
          }
          for (const row of document.querySelectorAll('.cards, .grid-2, .grid-3, .price-grid, .facts, .how-strip, .cta__facts')) {
            const kids = [...row.children].filter(k => k.offsetParent !== null);
            if (kids.length < 2) continue;
            const rb = row.getBoundingClientRect();
            const tops = [...new Set(kids.map(k => Math.round(k.getBoundingClientRect().top)))];
            if (tops.length < 2) continue;
            const last = kids.filter(k => Math.round(k.getBoundingClientRect().top) === tops[tops.length - 1]);
            const first = kids.filter(k => Math.round(k.getBoundingClientRect().top) === tops[0]);
            if (last.length < first.length) {
              const L = last[0].getBoundingClientRect().left - rb.left, R = rb.right - last[last.length - 1].getBoundingClientRect().right;
              if (Math.abs(L - R) > 30) issues.push(`row hole: ${row.className} (${first.length} then ${last.length}, left gap ${Math.round(L)} right gap ${Math.round(R)})`);
            }
          }
          for (const im of document.querySelectorAll('img')) if (im.complete && im.naturalWidth === 0) issues.push('broken image ' + im.getAttribute('src'));
          return issues;
        });
        for (const i of r) { problems++; console.log(`${u} @${w}: ${i}`); }
        await pg.close();
      }
    }
    console.log(`${problems} problems`);
  }
  await browser.close(); server.close();
  process.exit(problems ? 1 : 0);
})();
