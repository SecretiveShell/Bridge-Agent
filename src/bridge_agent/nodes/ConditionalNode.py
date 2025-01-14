from bridge_agent.models.workflow import ConditionalNode
from bridge_agent.models.context import Context, Message
from bridge_agent.openai_client import openai, model

async def RunConditionalNode(node: ConditionalNode, context: Context):
    outputs = "\n".join([f"- {output.value}" for output in node.outputs])
    prompt = f"Please evaluate the following condition: {node.condition}. The output should be one of the following options:\n{outputs}\nDo not include any other text."

    user_message = Message(role="user", content=prompt)
    context.history.append(user_message)

    response = await openai.chat.completions.create(
        model=model,
        messages=context.get_messages(),
    )

    assistant_message = Message(role="assistant", content=response.choices[0].message.content or "Assistant failed to respond.")
    context.history.append(assistant_message)
    
    for output in node.outputs:
        if output.value == response.choices[0].message.content:
            next_node = output.output
            break
    else:
        next_node = node.outputs[0].output

    return next_node, context
