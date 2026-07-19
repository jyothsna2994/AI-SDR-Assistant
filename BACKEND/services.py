from company_research import extract_domain, recommend_campaign
from email_generator import generate_email


def process_company(data):

    domain = extract_domain(data.website)

    campaign = recommend_campaign(data.company)
    
    email_data = generate_email(
    data.company,
    data.contact,
    campaign
)
    return {
    "company": data.company,
    "website": data.website,
    "domain": domain,
    "campaign": campaign,
    "subject": email_data["subject"],
    "email": email_data["email"],
    "followup1": email_data["followup1"],
    "followup2": email_data["followup2"],
    "followup3": email_data["followup3"],
    "contact": data.contact,
    "designation": data.designation,
    "status": "Information received successfully!"
} 