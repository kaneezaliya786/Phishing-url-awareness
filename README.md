# EWB Phishing URL Awareness Checker

## Overview

Phishing is a cyber attack where attackers disguise malicious links as trusted websites to steal sensitive information. This tool is an educational static text analyzer that inspects URLs for common phishing indicators without opening or probing live websites.

## Features

* Detects `@` symbols in URLs.
* Flags unusually long URLs (over 100 characters).
* Flags IP-address-based hostnames.
* Flags many hostname segments/subdomains (5 or more).
* Flags punycode-style hostnames (`xn--`).
* Flags the unencrypted HTTP scheme.
* **Improvement A:** Continuous loop (`while True`) with a `q` command to exit cleanly.
* **Improvement B:** Review carefully summary counter that counts active warnings.

## Requirements

* Python 3.14 (or any Python 3.x version)
* Uses standard built-in libraries (`urllib.parse`, `ipaddress`). No external packages are required (`requirements.txt` is intentionally empty).

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the script using the following command: `python phishing_checker.py`
4. Type a URL when prompted, or type `q` to quit.

## Example Output

EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result for: http://192.0.2.10/account
Warning signs found:
- URL uses an IP address instead of a familiar domain
- URL uses HTTP instead of HTTPS. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.

## Testing

Please refer to the detailed test log inside the `tests/test_samples.md` file.

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Uses an IP address instead of a familiar domain. Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol; inspect carefully. Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Contains a punycode-style hostname. | PASS |

## Screenshots

Screenshots of the program execution and testing evidence are stored in the `screenshots/` directory:
* `screenshots/sample_run.png` - Shows a terminal execution sample of the script running.
* `screenshots/test_results.png` - Shows testing logs and test case validation.

## Improvements

* **Loop with Quit Command:** Implemented a continuous `while` execution loop so users can check multiple URLs sequentially without restarting the script, with `q` serving as a safe exit command.
* **Review Summary Counter:** Added a helper function and counter to tally active warnings and display a clear summary prompt when risk indicators are detected.

## Limitations

* This tool is strictly educational and performs static text analysis only.
* It does not perform live website scanning, domain ownership verification, or internet requests.
* Finding no warning signs does **not** guarantee that a URL is safe.

## Ethical Use

This tool is designed strictly for defensive learning, awareness training, and safe analysis of sample strings. Do not use this tool for malicious scanning or probing.

## Author

* **Name:** Kaneez Aliya
* **Course:** Cybersecurity Mini Project (EWB)
