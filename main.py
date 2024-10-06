from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# প্রাথমিক স্টেট সেট করা হচ্ছে
status_list = [1, 0, 1, 1]

# স্টেট আপডেট করার জন্য একটি ডাটামডেল
class StatusUpdate(BaseModel):
    index: int
    value: int

# GET মেথড: বর্তমান স্টেট রিটার্ন করবে
@app.get("/status")
def get_status():
    return status_list

# POST মেথড: নির্দিষ্ট ইনডেক্সে স্টেট আপডেট করবে
@app.post("/status")
def update_status(update: StatusUpdate):
    if update.index < 0 or update.index >= len(status_list):
        raise HTTPException(status_code=400, detail="Index out of range")
    if update.value not in [0, 1]:
        raise HTTPException(status_code=400, detail="Value must be 0 or 1")
    
    status_list[update.index] = update.value
    return {"status": status_list}
