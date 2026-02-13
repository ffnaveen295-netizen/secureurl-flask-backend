import re

def extract_features(url):

    features = []

    features.append(len(url))
    features.append(1 if "https" in url else 0)
    features.append(url.count("."))
    features.append(1 if "@" in url else 0)
    features.append(url.count("-"))

    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    features.append(1 if re.search(ip_pattern, url) else 0)

    return features
