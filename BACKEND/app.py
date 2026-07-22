from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Company
from services import process_company

app = FastAPI(
    title="AI SDR Assistant",
    version="1.0"
)

# -------------------------
# CORS Configuration
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "https://ai-sdr-assistant.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    return process_company(data)








