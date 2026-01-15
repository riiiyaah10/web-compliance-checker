"""Cookie compliance checker"""


def check_cookies(response):
    return "Set-Cookie" in response.headers


def detect_cookie_banner(html):
    keywords = ["cookie", "cookies", "consent"]
    html_lower = html.lower()
    return any(word in html_lower for word in keywords)


class CookieChecker:
    """Checks website compliance with cookie regulations (GDPR, CCPA, etc.)"""
    
    def __init__(self):
        pass
    
    def check_cookies(self, url):
        """Check if website has proper cookie consent and notices"""
        pass
