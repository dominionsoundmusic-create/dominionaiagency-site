# Research notes: /missed-call-text-back/ (Oct 15 2026)

(WebFetch blocked in this container; facts confirmed from WebSearch results restricted to the official domains.)

## HighLevel missed call text back
- https://help.gohighlevel.com/support/solutions/articles/48001239140-where-and-how-to-configure-the-missed-call-text-back-feature
  Native setting in the phone system settings; write the message, test, save; ring timeout decides when a call
  counts as missed. Sends a text for every missed call, including repeat calls in a short window; suggested fix
  is a workflow with a wait step; do not run the native feature and a workflow together (duplicates).
- Call status workflow trigger: https://help.gohighlevel.com/support/solutions/articles/48001212511-call-status-workflow-trigger-setup
  Filter Direction = incoming, status = busy or no-answer.

## 10DLC and The Campaign Registry
- https://www.campaignregistry.com/ and TCR intro PDF https://www.campaignregistry.com/wp-content/uploads/TCR-Intro-2026-v4_comp.pdf
  TCR is the registry the mobile network operators chose to collect Brand and Campaign data for the 10DLC network;
  brands register through a messaging provider, not directly; the brand's EIN/Tax ID verifies identity;
  a Campaign is the use case of the messaging; carriers enable messaging by Campaign ID.
  Not used: review time ranges (older document), fees.

## CTIA Messaging Principles and Best Practices (July 2019)
- https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf
  Obtain appropriate consent before messaging; honor opt-outs; send one final opt-out confirmation and no
  further messages; STOP is the standardized opt-out word, but plain-language requests (stop, end, unsubscribe,
  cancel, quit, "please opt me out") should also be honored.

## FCC consent revocation
- FCC 24-24 / Federal Register, Strengthening the Ability of Consumers To Stop Robocalls:
  https://www.federalregister.gov/documents/2024/03/05/2024-04587/strengthening-the-ability-of-consumers-to-stop-robocalls
  Consumers may revoke consent by any reasonable means; replies such as "stop," "quit," "end," "revoke," "opt
  out," "cancel," or "unsubscribe" are per se reasonable; requests honored in a reasonable time not to exceed
  ten business days; one confirmation text allowed after an opt-out.
  Not used: effective dates of individual provisions (one was delayed by DA 25-312; status moving).
- FCC consumer guide: https://www.fcc.gov/consumers/guides/stop-unwanted-robocalls-and-texts

## Left out
- "missed call text back calculator" rows: a calculator would need invented lost-revenue assumptions; not built.
- "missed call called back number disconnected": a consumer phone question, not a buyer term.
- Any statistic about how fast customers expect a reply or how many go elsewhere: none verified.
