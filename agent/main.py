from fastapi import FastAPI, Request
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
# 🔥 Llama Router (ตัวหลัก)
# ---------------------------
def llama_router(prompt: str):
    router_prompt = f"""
You are a smart AI router.

Rules:
- If the task is simple, answer directly.
- If the task is complex, reasoning-heavy, or long → reply ONLY: USE_GEMINI

Prompt:
{prompt}
"""

    result = call_ollama(router_prompt)

    # ถ้า Llama บอกให้ใช้ Gemini
    if "USE_GEMINI" in result:
        return "gemini", call_gemini(prompt)

    # กันเคสตอบมั่ว/สั้นเกิน
    if len(result.strip()) < 30:
        return "gemini", call_gemini(prompt)

    return "ollama", result

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

@app.post("/api/chat")
async def chat_api(request: Request):
    body = await request.json()

    messages = body.get("messages", [])

    prompt = ""
    for msg in messages:
        role = msg.get("role", "")
        content = msg.get("content", "")
        prompt += f"{role}: {content}\n"

    try:
        model_used, answer = llama_router(prompt)

        return {
            "model": MODEL,
            "created_at": "2024-01-01T00:00:00Z",
            "message": {
                "role": "assistant",
                "content": f"[{model_used.upper()}]\n\n{answer}"
            },
            "done": True
        }

    except Exception as e:
        return {
            "message": {
                "role": "assistant",
                "content": f"Error: {str(e)}"
            },
            "done": True
        }

@app.get("/api/tags")
def ollama_tags():
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags")
        data = response.json()

        models = []
        for m in data.get("models", []):
            models.append({
                "name": m.get("name"),
                "model": m.get("name"),
                "modified_at": m.get("modified_at", ""),
                "size": m.get("size", 0),
                "digest": m.get("digest", ""),
                "details": m.get("details", {}),
                "version": "0.1.0"
            })

        return {
            "models": models
        }

    except Exception as e:
        return {
            "models": [],
            "error": str(e)
        }

@app.post("/api/generate")
async def generate(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")

    try:
        model_used, answer = llama_router(prompt)

        return {
            "response": f"[{model_used.upper()}]\n\n{answer}",
            "done": True
        }

    except Exception as e:
        return {
            "response": f"Error: {str(e)}",
            "done": True
        }

# ---------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
