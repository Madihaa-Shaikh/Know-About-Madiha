from abc import ABC, abstractmethod

class ChatModel(ABC):
    @abstractmethod
    def reply(self, message: str) -> str:
        """Return a response string for the given user message."""
        raise NotImplementedError