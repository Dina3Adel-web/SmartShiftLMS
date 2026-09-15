from fastapi import FastAPI

app = FastAPI(title="Smart Shift LMS")


@app.get("/")
def home():
    return {
        "platform": "Smart Shift LMS",
        "status": "running",
        "message": "Welcome to Smart Shift LMS 🚀"
    }
