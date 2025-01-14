from pydantic import BaseModel

class executeResponse(BaseModel):
    output: str
    chat_history: list[dict[str, str]]
