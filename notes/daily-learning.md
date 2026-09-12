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

