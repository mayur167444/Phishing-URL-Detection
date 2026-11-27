
import re
import math
from urllib.parse import urlparse

def extract_features(url):

    if not re.match(r"^https?://", url, re.IGNORECASE):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.hostname or ""
    full_url = url.lower()

    features = {}

    features["url_length"] = len(url)

    features["has_ip_address"] = 1 if re.match(
        r"^\d{1,3}(\.\d{1,3}){3}$", domain
    ) else 0

    features["dot_count"] = url.count(".")

    features["https_flag"] = 1 if parsed.scheme == "https" else 0

    features["url_entropy"] = 0
    if url:
        for char in set(url):
            probability = url.count(char) / len(url)
            features["url_entropy"] -= probability * math.log2(probability)

    features["token_count"] = len(re.findall(r"[a-zA-Z0-9]+", url))

    features["subdomain_count"] = max(0, len(domain.split(".")) - 2)

    features["query_param_count"] = len(parsed.query.split("&")) if parsed.query else 0

    tld = domain.split(".")[-1] if "." in domain else ""
    features["tld_length"] = len(tld)

    features["path_length"] = len(parsed.path)

    features["has_hyphen_in_domain"] = 1 if "-" in domain else 0

    features["number_of_digits"] = sum(char.isdigit() for char in url)

    features["tld_popularity"] = 0

    features["suspicious_file_extension"] = 1 if re.search(
        r"\.(exe|zip|scr|bat|msi|apk)$", parsed.path, re.IGNORECASE
    ) else 0

    features["domain_name_length"] = len(domain)

    features["percentage_numeric_chars"] = (
        sum(char.isdigit() for char in url) / len(url) * 100
        if url else 0
    )

    return features


if __name__ == "__main__":

    url = input("Enter URL: ")

    result = extract_features(url)

    print("\n===== URL FEATURE EXTRACTION =====")

    for feature, value in result.items():
        print(feature, ":", value)
