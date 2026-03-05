import requests
from src.domain.chat_model import ChatModel

class GeneralChatModel(ChatModel):
    def __init__(self, model_name: str = "phi3:latest"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/chat"

    def reply(self, message: str) -> str:
        msg = (message or "").strip()
        if not msg:
            return "Please type something."

        try:
            payload = {
                "model": self.model_name,
                "messages": [{"role": "user", "content": msg}],
                "stream": False
            }
            r = requests.post(self.url, json=payload, timeout=60)
            r.raise_for_status()
            data = r.json()
            return data["message"]["content"]

        except Exception as e:
            return (
                "Couldn't reach Ollama at http://localhost:11434.\n"
                "Make sure Ollama is running.\n\n"
                f"Error: {e}"
            )