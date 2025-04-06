from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS so your Chrome extension can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "chrome-extension://lclgpbfnlejbmddonjeijhmlnlncepkk"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AutomationRequest(BaseModel):
    id: str
    password: str
    action: str

@app.post("/run-task")
async def run_task(data: AutomationRequest):
    # You can plug in your selenium logic here
    print(f"Received automation request: {data}")

    # Simulate response
    return {"message": f"Action '{data.action}' started for ID '{data.id}'"}
