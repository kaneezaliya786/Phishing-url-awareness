
# Phishing URL Checker - Test Samples

These tests are for educational awareness. The program checks URL text only and does not open links.

## Test 1: HTTP URL
Input: http://example.com
Expected warning: URL uses HTTP instead of HTTPS.

## Test 2: HTTPS URL
Input: https://example.com
Expected warning signs: None of the six checks should trigger.

## Test 3: URL containing @
Input: http://example.com@fake.com
Expected warning: URL contains an @ symbol.

## Test 4: Long URL
Input: A URL longer than 100 characters.
Expected warning: URL is longer than 100 characters.

## Test 5: Punycode hostname
Input: http://xn--example-ova.com
Expected warning: Hostname contains a punycode marker.

## Important
Expected results must be verified by running the program. No warning signs detected does not guarantee that a URL is safe.
