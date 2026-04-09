from fastapi import FastAPI
import os
import requests
import uvicorn

app = FastAPI(title="AI Local Agent")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "llama3.1:8b-instruct-q4_K_M")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ---------------------------
# Helper: Ollama
# ---------------------------
def call_ollama(prompt: str):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# ---------------------------
# Helper: Gemini
# ---------------------------
def call_gemini(prompt: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GOOGLE_API_KEY}"
    response = requests.post(
        url,
        json={
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }
    )
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]

# ---------------------------
# Smart Router
# ---------------------------
def choose_model(prompt: str):
    if len(prompt) > 1500:
        return "gemini"
    if "analyze" in prompt or "reason" in prompt:
        return "gemini"
    return "ollama"

# ---------------------------
# Routes
# ---------------------------
@app.get("/")
def read_root():
    return {
        "status": "online",
        "model": MODEL,
        "ollama_url": OLLAMA_URL
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/chat")
def chat(prompt: str):
    model_choice = choose_model(prompt)

    try:
        if model_choice == "gemini":
            answer = call_gemini(prompt)
        else:
            answer = call_ollama(prompt)

        return {
            "model_used": model_choice,
            "response": answer
        }

    except Exception as e:
        return {
            "error": str(e),
            "fallback": "ollama"
        }

# ---------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
