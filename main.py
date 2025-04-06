from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    return {"message": f"Received request to perform '{data.action}' on {data.url} for ID '{data.id}'"}
