from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="OpenAI-Compatible Adapter", version="0.1.0")


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str
    messages: list[ChatMessage]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/v1/models")
def models() -> dict:
    return {
        "object": "list",
        "data": [
            {"id": "qwen2.5:7b", "object": "model"},
            {"id": "mixtral:8x7b", "object": "model"},
        ],
    }


@app.post("/v1/chat/completions")
def chat_completions(payload: ChatRequest) -> dict:
    user_text = " ".join(m.content for m in payload.messages if m.role == "user").strip()
    content = f"Mock response from {payload.model}: {user_text or 'hello'}"
    return {
        "id": "chatcmpl-mock-001",
        "object": "chat.completion",
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": content},
                "finish_reason": "stop",
            }
        ],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
