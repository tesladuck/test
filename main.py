from fastapi import FastAPI
from pydantic import BaseModel
from Crypto.Cipher import AES
import base64
import hashlib

app = FastAPI()

SECRET_KEY = 'MySuperSecretKey!'

class RequestData(BaseModel):
    id: str
    password: str
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
    decrypted_id = decrypt(data.id)
    decrypted_password = decrypt(data.password)

    return {
        "id": decrypted_id,
        "password": decrypted_password,
        "action": data.action
    }
