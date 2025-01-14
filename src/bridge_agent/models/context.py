from pydantic import BaseModel, Field

class Message(BaseModel):
    role: str = Field(..., description="The role of the message")
    content: str = Field(..., description="The content of the message")

class Context(BaseModel):
    id: str = Field(..., description="Unique identifier for the context")
    history: list[Message] = Field(..., description="chat message history")

    def get_messages(self) -> list[dict[str, str]]:
        messages = []
        for message in self.history:
            messages.append({"role": message.role, "content": message.content})
        return messages