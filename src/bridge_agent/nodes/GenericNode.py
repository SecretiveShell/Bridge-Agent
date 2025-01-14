from bridge_agent.models.workflow import GenericNode
from bridge_agent.models.context import Context, Message
from bridge_agent.openai_client import openai, model

async def RunGenericNode(node: GenericNode, context: Context):
    prompt = f"Please execute the following action: {node.action}\n\nUse tools if available, and if not use your best judgement/common sense."

    user_message = Message(role="user", content=prompt)
    context.history.append(user_message)

    response = await openai.chat.completions.create(
        model=model,
        messages=context.get_messages()
    )

    assistant_message = Message(role="assistant", content=response.choices[0].message.content or "Assistant failed to respond.")
    context.history.append(assistant_message)
    
    return node.output, context
