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

    self.url = "https://spandan.indianoil.co.in/RetailNew/Login.jsp"
    self.headers = {
        "Cookie": (
            "JSESSIONID=3occIY7-6lNTBCvH0zmfYPUbKs8AKQOdcDCcA13n.mudvappjbprd02; "
            "TS01b06107=0120e46af1ccf522e2b4edc74063f22b6406be6578bb804c348dbea81b491348459dc0aed58abc8c1d9f303889a48dd014b77c6075; "
            "BIGipServerJboss_52.53_8080=893489674.36895.0000; "
            "TS015c0662=0120e46af1ccf522e2b4edc74063f22b6406be6578bb804c348dbea81b491348459dc0aed58abc8c1d9f303889a48dd014b77c6075"
        )
    }
        
    check_dashboard(self)

# task_handler.py
    def check_dashboard(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            content = response.text

            if "Retail Dashboard" in content:
                session_cookies = response.cookies.get_dict()
                relevant_cookies = {k: v for k, v in session_cookies.items() if k in [
                    "TS01b06107", "JSESSIONID", "BIGipServerJboss_52.53_8080", "TS015c0662"
                ]}
                return {
                    "status": "success",
                    "message": "Retail Dashboard loaded successfully.",
                    "cookies": relevant_cookies
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
