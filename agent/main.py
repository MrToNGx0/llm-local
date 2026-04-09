from fastapi import FastAPI
import os
import requests
import uvicorn

app = FastAPI(title="AI Local Agent")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "model": os.getenv("MODEL"),
        "ollama_url": os.getenv("OLLAMA_URL")
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
