from openai import AsyncOpenAI
from bridge_agent.config import config

openai: AsyncOpenAI = AsyncOpenAI(
    api_key=config.openai_api_key,
    base_url=config.openai_base_url,
)

model = config.openai_model
