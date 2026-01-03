from banner import show_banner
from rules import (
    is_ip_url,
    has_https,
    has_suspicious_keywords,
    is_fake_domain
)

def analyze_url(url):
    score = 0
    reasons = []

    if is_ip_url(url):
        score += 2
        reasons.append("IP-based URL detected")

    if not has_https(url):
        score += 1
        reasons.append("HTTPS missing")

    if has_suspicious_keywords(url):
        score += 1
        reasons.append("Suspicious keywords found")

    if is_fake_domain(url):
        score += 1
        reasons.append("Suspicious domain structure")

    return score, reasons

def verdict(score):
    if score >= 4:
        return "🚨 PHISHING (High Risk)"
    elif score >= 2:
        return "⚠️ SUSPICIOUS"
    else:
        return "✅ SAFE"

if __name__ == "__main__":
    show_banner()

    url = input("🔗 Enter URL to analyze: ").strip()
    score, reasons = analyze_url(url)

    print("\n📊 Analysis Result")
    print("-" * 30)
    print(f"Verdict : {verdict(score)}")
    print(f"Risk Score : {score}")

    if reasons:
        print("\nReasons:")
        for r in reasons:
            print(f"- {r}")
    else:
        print("No suspicious signs detected")

    print("\n👍 Stay Safe Online!")
