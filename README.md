
# Phishing URL Awareness Checker

## Project Description
This is a beginner-friendly Python project that checks URL text for common phishing warning signs.

## Features
The program checks for six warning signs:
1. The presence of an @ symbol
2. URLs longer than 100 characters
3. IP addresses used as hostnames
4. Hostnames with five or more segments
5. Punycode markers such as xn--
6. HTTP instead of HTTPS

## Technologies Used
- Python 3
- GitHub

## How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

   python phishing_checker.py

4. Enter a URL when prompted.

## Important Note
This project is for educational awareness only. It checks URL text and does not open or scan links. No warning signs detected does not guarantee that a URL is safe.
