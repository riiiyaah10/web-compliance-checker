"""Main scanner module for web compliance checking"""

import requests
from checker.cookie_checker import check_cookies, detect_cookie_banner
from checker.privacy_checker import privacy_policy_exists, terms_exists
from checker.security_checker import check_https, security_headers
from report import generate_report

def scan_website(url):
    response = requests.get(url)
    html = response.text

    data = {
        "https_enabled": check_https(url),
        "cookies_used": check_cookies(response),
        "cookie_banner_detected": detect_cookie_banner(html),
        "privacy_policy_found": privacy_policy_exists(url),
        "terms_found": terms_exists(url),
    }

    data.update(security_headers(response))
    return generate_report(data)


if __name__ == "__main__":
    website = input("Enter website URL: ")
    result = scan_website(website)
    print("\nCompliance Report:")
    for key, value in result.items():
        print(f"{key}: {value}")
