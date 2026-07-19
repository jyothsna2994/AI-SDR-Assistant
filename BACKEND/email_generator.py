from prompts import GENERIC_EMAIL_PROMPT

def generate_subject(campaign):

    if campaign == "Generic Enterprise Automation":
        return "Simplify Test Automation Across Web, Mobile & APIs"

    elif campaign == "Banking Automation":
        return "Accelerate Banking QA with Agentic AI"

    elif campaign == "Insurance Automation":
        return "Modernize Insurance Testing with AI"

    else:
        return "Accelerate Test Automation with ACCELQ"

def generate_email(company, contact, campaign):

    subject = "Simplify Test Automation Across Web, Mobile & APIs"

    email = f"""Hi {contact},

As {company} continues to accelerate digital transformation, maintaining reliable test automation across Web, Mobile, and APIs can become increasingly challenging.

ACCELQ's Agentic AI-powered automation platform helps teams improve test coverage, reduce maintenance, and accelerate releases.

Would you be available for a quick discussion next week?

Best regards,
Emma
"""

    followup1 = f"""Hi {contact},

Just following up on my previous email.

I wanted to check if improving automation efficiency at {company} is currently a priority.

I'd be happy to schedule a quick demo whenever convenient.

Best regards,
Emma
"""

    followup2 = f"""Hi {contact},

I understand you're busy.

Many organizations like {company} have reduced testing effort and improved release quality using ACCELQ.

Would next week be a good time for a short conversation?

Best regards,
Emma
"""

    followup3 = f"""Hi {contact},

This will be my final follow-up.

If AI-powered test automation becomes a priority at {company}, I'd be happy to reconnect in the future.

Thank you for your time.

Best regards,
Emma
"""

    return {
        "subject": subject,
        "email": email,
        "followup1": followup1,
        "followup2": followup2,
        "followup3": followup3
    }