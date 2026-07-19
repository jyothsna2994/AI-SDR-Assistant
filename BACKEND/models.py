from pydantic import BaseModel

class Company(BaseModel):
    company: str
    website: str
    contact: str
    designation: str