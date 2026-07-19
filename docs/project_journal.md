# AI SDR Assistant Project Journal

## Day 1
- Project initialized
- Installed Python, Git, Node.js
- Created project folder structure

## Day 2
- Installed FastAPI and Uvicorn
- Created first FastAPI application
- Learned how to run a backend server
- Learned what an API is
- Successfully accessed the API in the browser

## Day 3
- Learned GET and POST APIs
- Created first POST endpoint
- Learned Request Body and Response Body
- Tested APIs using Swagger UI
- Learned about BaseModel
- Learned FastAPI validation

## Day 4
- Extended the Company model
- Added website, contact, and designation fields
- Learned how FastAPI validates multiple fields
- Successfully accepted complete prospect information
- Understood how JSON data is sent to the backend
- Learned how API responses are returned dynamically

## Day 5
- Learned project structure
- Created models.py
- Moved Company model to a separate file
- Imported Company model into app.py
- Learned Separation of Concerns
- Understood why professional projects use multiple modules

## Day 6

### What I Built
- Used company_research.py
- Created extract_domain()
- Imported a function into app.py
- Processed website URLs

### What I Learned
- Python modules
- Importing functions
- urllib.parse
- Function calls
- Separation of business logic

## Day 7

### What I Built
- Added recommend_campaign() function
- Used if-elif-else for campaign selection
- Imported multiple functions from company_research.py
- Returned campaign recommendation in the API response

### What I Learned
- Decision making using if-elif-else
- String matching with "in"
- Using lower() for case-insensitive comparison
- Keeping business logic separate from API routes

### Challenges Faced
- Forgot to call recommend_campaign()
- Learned how to debug and fix the API

## Day 8

### What I Built
- Created services.py
- Created process_company()
- Moved business workflow from app.py
- Used service layer architecture

### What I Learned
- What a Service Layer is
- Why enterprise applications separate responsibilities
- How app.py becomes cleaner using services

## Day 9

### What I Built
- Created email_generator.py
- Generated email subject
- Generated email body
- Connected email generation with services.py

### What I Learned
- Returning dictionaries from functions
- Organizing code into separate modules
- Building reusable email templates

## Day 10

### What I Built
- Added multiple email templates
- Created Banking and Insurance templates
- Used campaign-based template selection
- Generated different subjects automatically

### What I Learned
- Conditional template selection
- Reusable email generation logic
- Building scalable outreach templates

## Day 11

### What I Built
- Used prompts.py
- Created GENERIC_EMAIL_PROMPT
- Imported prompt into email_generator.py

### What I Learned
- What AI prompts are
- Why prompts should be separated
- Preparing architecture for AI integration