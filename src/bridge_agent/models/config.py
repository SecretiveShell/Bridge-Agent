from pydantic import BaseModel

class Config(BaseModel):
    openai_api_key: str
    openai_model: str = "gpt-3.5-turbo"
    openai_base_url: str = "https://api.openai.com/v1"