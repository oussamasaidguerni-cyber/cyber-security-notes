## 2026-10-04

- **Topic:** WebDAV
- **Note:** If OPTIONS reveals PUT/DELETE, check if .txt.php or trailing-dot files bypass the parser

---

## 2026-10-03

- **Topic:** File Upload
- **Note:** Test extension case/polyglot: .phtml, .php5, .phar and double-extension bypass filters cheaply

---

## 2026-10-02

- **Topic:** Rate Limiting
- **Note:** Two-stage auth bypass: many apps rate-limit password tries but not the 2FA/OTP field

---

## 2026-10-01

- **Topic:** Headers
- **Note:** Scan for missing HSTS/Content-Security-Policy on any target - easy finding categories for bug bounties

---

## 2026-09-30

- **Topic:** CORS
- **Note:** Reflected Origin + ACAO: * : combined with credentials cookies is a classic data-exfil bug class

---

## 2026-09-29

- **Topic:** Deserialization
- **Note:** Check which libraries/plugins the app uses - known gadget chains beat fuzzing blindness

---

## 2026-09-28

- **Topic:** Networking
- **Note:** For a quick service overview, 'nmap -sV -sC -p-' on small ranges beats running separate tools

---

## 2026-09-27

- **Topic:** Fuzzing
- **Note:** ffuf -ac auto-calibrates to filter default responses - much cleaner results on custom apps

---

## 2026-09-26

- **Topic:** Auth
- **Note:** JWT alg confusion: try 'none' and RS256->HS256 swaps before hunting elsewhere

---

## 2026-09-25

- **Topic:** IDOR
- **Note:** Burp macros + session rules can auto-fetch fresh tokens between Intruder requests when testing IDOR

---

## 2026-09-24

- **Topic:** Burp Suite
- **Note:** Use Match/Replace rules in Burp to auto-append headers (e.g. X-Forwarded-For) to every request

---

## 2026-09-23

- **Topic:** XSS
- **Note:** Test every reflection point's encoder: the same payload works differently in HTML, attribute, JS and URL contexts

---

## 2026-09-22

- **Topic:** SQLi
- **Note:** Always test numeric params with arithmetic first (e.g. ?id=2-1 returns item 1) before reaching for sqlmap

---

## 2026-09-21

- **Topic:** Recon
- **Note:** crt.sh JSON API gives historical subdomains for free. Pipe through jq and sort -u to find takeover targets

---

## 2026-09-20

- **Topic:** Logging
- **Note:** Mass-assignment via JSON body: send {'role':'admin'} or {'isAdmin':true} and watch dev frameworks accept it

---

## 2026-09-19

- **Topic:** Open Redirect
- **Note:** Check //evil.com and /\evil.com rewrites - simple filter bypasses that turn into OAuth token theft

---

## 2026-09-18

- **Topic:** SSRF
- **Note:** Test URL params with localhost/169.254.169.254; many firewalls only block public IPs

---

## 2026-09-17

- **Topic:** Password Reset
- **Note:** Host header poisoning on password reset links is still a top payout bug - always test it

---

## 2026-09-16

- **Topic:** JS Analysis
- **Note:** Grep every JS bundle for /api/, apiKey, secret, token - developers leave endpoints in client code

---

## 2026-09-15

- **Topic:** DNS
- **Note:** Check for subdomain takeovers via canonical-name records pointing at expired cloud services

---

## 2026-09-14

- **Topic:** WebDAV
- **Note:** If OPTIONS reveals PUT/DELETE, check if .txt.php or trailing-dot files bypass the parser

---

## 2026-09-13

- **Topic:** File Upload
- **Note:** Test extension case/polyglot: .phtml, .php5, .phar and double-extension bypass filters cheaply

---

## 2026-09-12

- **Topic:** Rate Limiting
- **Note:** Two-stage auth bypass: many apps rate-limit password tries but not the 2FA/OTP field

---

## 2026-09-11

- **Topic:** Headers
- **Note:** Scan for missing HSTS/Content-Security-Policy on any target - easy finding categories for bug bounties

---

# Daily Security Learning Journal

One curated note per day - keeping the streak honest.

---

## 2026-09-10

- **Topic:** CORS
- **Note:** Reflected Origin + ACAO: * : combined with credentials cookies is a classic data-exfil bug class

---

## 2026-09-09

- **Topic:** Deserialization
- **Note:** Check which libraries/plugins the app uses - known gadget chains beat fuzzing blindness

---

## 2026-09-08

- **Topic:** Networking
- **Note:** For a quick service overview, 'nmap -sV -sC -p-' on small ranges beats running separate tools

---

## 2026-09-07

- **Topic:** Fuzzing
- **Note:** ffuf -ac auto-calibrates to filter default responses - much cleaner results on custom apps

---

## 2026-09-06

- **Topic:** Auth
- **Note:** JWT alg confusion: try 'none' and RS256->HS256 swaps before hunting elsewhere

---

## 2026-09-05

- **Topic:** IDOR
- **Note:** Burp macros + session rules can auto-fetch fresh tokens between Intruder requests when testing IDOR

---

## 2026-09-04

- **Topic:** Burp Suite
- **Note:** Use Match/Replace rules in Burp to auto-append headers (e.g. X-Forwarded-For) to every request

---

## 2026-09-03

- **Topic:** XSS
- **Note:** Test every reflection point's encoder: the same payload works differently in HTML, attribute, JS and URL contexts

---

## 2026-09-02

- **Topic:** SQLi
- **Note:** Always test numeric params with arithmetic first (e.g. ?id=2-1 returns item 1) before reaching for sqlmap

---

## 2026-09-01

- **Topic:** Recon
- **Note:** crt.sh JSON API gives historical subdomains for free. Pipe through jq and sort -u to find takeover targets

---

