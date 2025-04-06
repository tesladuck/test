from fastapi import FastAPI
from pydantic import BaseModel
from Crypto.Cipher import AES
import base64
import hashlib

app = FastAPI()

SECRET_KEY = 'ZNlTGrenm1cCW1jt'  # Match with frontend

class RequestData(BaseModel):
    encryptedId: str
    encryptedPassword: str
    action: str

def decrypt(ciphertext):
    key = hashlib.sha256(SECRET_KEY.encode()).digest()
    raw_data = base64.b64decode(ciphertext)
    iv = raw_data[:16]
    encrypted = raw_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    return decrypted.rstrip(b"\0").decode('utf-8')

@app.post("/run-task")
async def run_task(data: RequestData):
    decrypted_id = decrypt(data.encryptedId)
    decrypted_password = decrypt(data.encryptedPassword)

    return {
        "encryptedId": decrypted_id,
        "encryptedPassword": decrypted_password,
        "action": data.action
    }
