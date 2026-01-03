import socket
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "secure", "account",
    "update", "free", "bonus", "confirm"
]

def is_ip_url(url):
    try:
        hostname = urlparse(url).hostname
        socket.inet_aton(hostname)
        return True
    except:
        return False

def has_https(url):
    return url.startswith("https://")

def has_suspicious_keywords(url):
    for word in SUSPICIOUS_KEYWORDS:
        if word in url.lower():
            return True
    return False

def is_fake_domain(url):
    parsed = urlparse(url)
    if parsed.hostname and parsed.hostname.count("-") >= 3:
        return True
    return False
