from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI SDR Assistant",
    version="1.0"
)

# -------------------------
# Request Model
# -------------------------

class Company(BaseModel):
    company: str
    website: str
    contact: str
    designation: str


# -------------------------
# Home API
# -------------------------

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "🚀 AI SDR Assistant Backend is Running!"
    }


# -------------------------
# Company API
# -------------------------

@app.post("/company")
def company_info(data: Company):

   return {
    "company": data.company,
    "website": data.website,
    "contact": data.contact,
    "designation": data.designation,
    "status": "Information received successfully!"
    }
