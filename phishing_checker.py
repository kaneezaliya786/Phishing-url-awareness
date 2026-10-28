
from urllib.parse import urlparse
import ipaddress


def check_url(url):
    warnings = []

    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    if "@" in url:
        warnings.append("URL contains an @ symbol")

    if len(url) > 100:
        warnings.append("URL is longer than 100 characters")

    try:
        ipaddress.ip_address(hostname)
        warnings.append("URL uses an IP address as its hostname")
    except ValueError:
        pass

    if len(hostname.split(".")) >= 5:
        warnings.append("Hostname has 5 or more segments")

    if "xn--" in hostname.lower():
        warnings.append("Hostname contains a punycode marker")

    if parsed.scheme.lower() == "http":
        warnings.append("URL uses HTTP instead of HTTPS")

    print("\nURL:", url)

    if warnings:
        print("Warning signs found:")
        for warning in warnings:
            print("-", warning)
    else:
        print("No warning signs detected.")
        print("This does not guarantee that the URL is safe.")


if __name__ == "__main__":
    user_url = input("Enter a URL to check: ").strip()
    check_url(user_url)
