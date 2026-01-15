"""Privacy policy compliance checker"""

import requests

def check_page_exists(base_url, paths):
    for path in paths:
        try:
            r = requests.get(f"{base_url}/{path}", timeout=5)
            if r.status_code == 200:
                return True
        except:
            continue
    return False


def privacy_policy_exists(url):
    return check_page_exists(url, ["privacy", "privacy-policy"])


def terms_exists(url):
    return check_page_exists(url, ["terms", "terms-and-conditions"])


class PrivacyChecker:
    """Checks website compliance with privacy policy requirements"""
    
    def __init__(self):
        pass
    
    def check_privacy_policy(self, url):
        """Check if website has a privacy policy"""
        pass
