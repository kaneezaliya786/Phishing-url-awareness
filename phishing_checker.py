import urllib.parse
import ipaddress

def check_url(url):
    warnings = []
    
    # Basic check for @ symbol
    if "@" in url:
        warnings.append("Contains an @ symbol; inspect carefully")
        
    # Check for long URLs
    if len(url) > 100:
        warnings.append("URL is unusually long (over 100 characters)")
        
    try:
        parsed = urllib.parse.urlparse(url)
        hostname = parsed.hostname
        
        if hostname:
            # Check for IP address in hostname
            try:
                ipaddress.ip_address(hostname)
                warnings.append("URL uses an IP address instead of a familiar domain")
            except ValueError:
                pass
                
            # Check for many hostname segments
            if hostname.count('.') >= 4:
                warnings.append("Contains many hostname segments/subdomains")
                
            # Check for punycode
            if "xn--" in hostname:
                warnings.append("Contains a punycode-style hostname")
                
        # Check HTTP scheme
        if parsed.scheme.lower() == "http":
            warnings.append("URL uses HTTP instead of HTTPS. HTTPS alone does not prove trust.")
            
    except Exception:
        warnings.append("Could not identify or parse URL structure")
        
    return warnings

def has_warnings(findings):
    # Helper to check if actual warnings are found
    info_messages = ("No warning signs detected", "Could not identify")
    return not any(f.startswith(info_messages) for f in findings)

def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")
    
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ").strip()
        
        if raw_url.lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break
            
        if not raw_url:
            print("No URL entered.")
            continue
            
        print(f"\nResult for: {raw_url}")
        findings = check_url(raw_url)
        
        if findings:
            print("Warning signs found:")
            for item in findings:
                print("-", item)
        else:
            print("- No listed warning signs found. This does NOT prove safety.")
            
        # Improvement 2: Review carefully summary count
        if has_warnings(findings):
            print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")
        print("Never enter passwords from unexpected links.")

if __name__ == "__main__":
    main()
