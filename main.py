from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = FastAPI()

# Enable CORS (important for Chrome extension to call the API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your extension origin for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected request format
class AutomationRequest(BaseModel):
    url: str
    id: str
    password: str
    action: str

@app.post("/run-task")
async def run_task(data: AutomationRequest):
    # Debug output - Replace with actual automation logic
    print(f"Received Automation Request:")
    print(f"URL: {data.url}")
    print(f"User ID: {data.id}")
    print(f"Password: {data.password}")
    print(f"Action: {data.action}")

    # Respond back
    print(f"Received request to perform '{data.action}' on {data.url} for ID '{data.id}'")

    result = check_retail_dashboard()
    print(f"Result: '{result}'")
    return result

# task_handler.py
def check_retail_dashboard():
    proxies = {
        "http": "http://204.236.137.68:80",
        "https": "http://204.236.137.68:80",
    }
    
    url = "https://spandan.indianoil.co.in/RetailNew/Login.jsp"
    
    headers = {
        "Host": "spandan.indianoil.co.in",
        "Origin": "https://spandan.indianoil.co.in"
    }
    
    response = requests.get(url, headers=headers, proxies=proxies, timeout=15, verify=False)
    
    if "Retail Dashboard" in response.text:
        # Extract cookies in desired format
        cookies = response.cookies.get_dict()
        formatted_cookies = "; ".join([f"{k}={v}" for k, v in cookies.items()
                                       if k in ["TS01b06107", "JSESSIONID", "BIGipServerJboss_52.53_8080", "TS015c0662"]])
        print("✅ Site Accessed!")
        print("Cookies:", formatted_cookies)
    else:
        print("❌ Retail Dashboard not found.")
