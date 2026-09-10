#!/usr/bin/env python3
"""Daily security learning journal - appends one curated note per day."""

import os
from datetime import datetime, timedelta, timezone

NOTES_DIR = "notes"
NOTES_FILE = os.path.join(NOTES_DIR, "daily-learning.md")

TIPS = [
    {"topic": "Recon", "tip": "crt.sh JSON API gives historical subdomains for free. Pipe through jq and sort -u to find takeover targets"},
    {"topic": "SQLi", "tip": "Always test numeric params with arithmetic first (e.g. ?id=2-1 returns item 1) before reaching for sqlmap"},
    {"topic": "XSS", "tip": "Test every reflection point's encoder: the same payload works differently in HTML, attribute, JS and URL contexts"},
    {"topic": "Burp Suite", "tip": "Use Match/Replace rules in Burp to auto-append headers (e.g. X-Forwarded-For) to every request"},
    {"topic": "IDOR", "tip": "Burp macros + session rules can auto-fetch fresh tokens between Intruder requests when testing IDOR"},
    {"topic": "Auth", "tip": "JWT alg confusion: try 'none' and RS256->HS256 swaps before hunting elsewhere"},
    {"topic": "Fuzzing", "tip": "ffuf -ac auto-calibrates to filter default responses - much cleaner results on custom apps"},
    {"topic": "Networking", "tip": "For a quick service overview, 'nmap -sV -sC -p-' on small ranges beats running separate tools"},
    {"topic": "Deserialization", "tip": "Check which libraries/plugins the app uses - known gadget chains beat fuzzing blindness"},
    {"topic": "CORS", "tip": "Reflected Origin + ACAO: * : combined with credentials cookies is a classic data-exfil bug class"},
    {"topic": "Headers", "tip": "Scan for missing HSTS/Content-Security-Policy on any target - easy finding categories for bug bounties"},
    {"topic": "Rate Limiting", "tip": "Two-stage auth bypass: many apps rate-limit password tries but not the 2FA/OTP field"},
    {"topic": "File Upload", "tip": "Test extension case/polyglot: .phtml, .php5, .phar and double-extension bypass filters cheaply"},
    {"topic": "WebDAV", "tip": "If OPTIONS reveals PUT/DELETE, check if .txt.php or trailing-dot files bypass the parser"},
    {"topic": "DNS", "tip": "Check for subdomain takeovers via canonical-name records pointing at expired cloud services"},
    {"topic": "JS Analysis", "tip": "Grep every JS bundle for /api/, apiKey, secret, token - developers leave endpoints in client code"},
    {"topic": "Password Reset", "tip": "Host header poisoning on password reset links is still a top payout bug - always test it"},
    {"topic": "SSRF", "tip": "Test URL params with localhost/169.254.169.254; many firewalls only block public IPs"},
    {"topic": "Open Redirect", "tip": "Check //evil.com and /\\evil.com rewrites - simple filter bypasses that turn into OAuth token theft"},
    {"topic": "Logging", "tip": "Mass-assignment via JSON body: send {'role':'admin'} or {'isAdmin':true} and watch dev frameworks accept it"},
]

TIP_INDEX = datetime.now(timezone.utc).toordinal() % len(TIPS)


def init_file(notes_file):
    if not os.path.exists(notes_file):
        os.makedirs(os.path.dirname(notes_file), exist_ok=True)
        with open(notes_file, "w") as f:
            f.write("# Daily Security Learning Journal\n\n")
            f.write("One curated note per day - keeping the streak honest.\n\n")
            f.write("---\n\n")


def read_file(notes_file):
    with open(notes_file) as f:
        return f.read()


def take_snapshot(tip):
    today = datetime.now(timezone.utc).date()
    return (
        "## " + today.isoformat() + "\n\n"
        "- **Topic:** " + tip["topic"] + "\n"
        "- **Note:** " + tip["tip"] + "\n\n"
        "---\n\n"
    )


def main():
    init_file(NOTES_FILE)
    content = read_file(NOTES_FILE)
    today = datetime.now(timezone.utc).date()

    if today.isoformat() in content:
        print("Already updated today, nothing to write.")
        return 0

    tip = TIPS[TIP_INDEX]
    snapshot = take_snapshot(tip)

    with open(NOTES_FILE, "w") as f:
        f.write(snapshot + content)

    print("Wrote note for", today.isoformat())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())