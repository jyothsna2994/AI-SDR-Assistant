from urllib.parse import urlparse


def extract_domain(url: str):

    parsed = urlparse(url)

    return parsed.netloc

def recommend_campaign(company: str):

    company = company.lower()

    if "bank" in company:
        return "Banking Automation"

    elif "telecom" in company:
        return "Generic Enterprise Automation"

    elif "insurance" in company:
        return "Insurance Automation"

    else:
        return "Enterprise Test Automation"