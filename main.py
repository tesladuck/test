from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

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
    url = "https://spandan.indianoil.co.in/RetailNew/Login.jsp"

    headers = {
        "Host": "spandan.indianoil.co.in",
        "Origin": "https://spandan.indianoil.co.in",
        "User-Agent": "PostmanRuntime/7.43.3",  # Pretend it's a browser
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers)
        content = response.text

        if "Retail Dashboard" in content:
            cookies = response.cookies.get_dict()

            keys = ["TS01b06107", "JSESSIONID", "BIGipServerJboss_52.53_8080", "TS015c0662"]
            cookie_str = "; ".join([f"{key}={cookies.get(key, '')}" for key in keys])

            return {
                "status": "success",
                "message": "Retail Dashboard loaded successfully.",
                "cookie_string": cookie_str
            }
        else:
            return {
                "status": "fail",
                "message": "Retail Dashboard not found in response."
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
