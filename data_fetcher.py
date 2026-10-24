import requests
import os

CRUSTDATA_API_KEY = os.getenv("CRUSTDATA_API_KEY", "MOCK_KEY")

def get_company_signals(company_name: str):
    """Fetches headcount growth & stack context from Crustdata."""
    if CRUSTDATA_API_KEY == "MOCK_KEY":
        # Fallback Mock data for fast hacking
        return {
            "company": company_name,
            "engineering_headcount_growth_6m": "35%",
            "top_tech_stack": ["Python", "FastAPI", "PostgreSQL", "Docker"],
            "avg_tenure_years": 2.1
        }
    
    # Real Crustdata API Call
    url = "https://api.crustdata.com/screener/person/search"
    headers = {"Authorization": f"Bearer {CRUSTDATA_API_KEY}"}
    payload = {"company_name": company_name}
    res = requests.post(url, json=payload, headers=headers)
    return res.json() if res.status_code == 200 else {}