from bridge_agent.models.workflow import EndNode
from bridge_agent.models.context import Context, Message
from bridge_agent.openai_client import openai, model

async def RunEndNode(node: EndNode, context: Context):
    return context.history[-1].content