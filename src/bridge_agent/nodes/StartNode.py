import secrets
from bridge_agent.models.workflow import StartNode
from bridge_agent.models.context import Context, Message

async def RunStartNode(node: StartNode):
    return node.output, Context(id=secrets.token_hex(16), history=[Message(role="system", content="You are a helpful assistant.")])