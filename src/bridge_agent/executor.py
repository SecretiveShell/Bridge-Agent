from bridge_agent.models.executeResponse import executeResponse
from bridge_agent.models.workflow import AgenticWorkflowSchema, ConditionalNode, EndNode, GenericNode, StartNode
from bridge_agent.nodes.EndNode import RunEndNode
from bridge_agent.nodes.StartNode import RunStartNode
from bridge_agent.nodes.GenericNode import RunGenericNode
from bridge_agent.nodes.ConditionalNode import RunConditionalNode

async def RunWorkflow(workflow: AgenticWorkflowSchema):
    for node in workflow.nodes:
        if node.type == "StartNode":
            start_node = node
            break
    else:
        raise ValueError("No start node found in workflow")
    
    assert isinstance(start_node, StartNode)
    next_node_id, context = await RunStartNode(start_node)

    while True:
        for node in workflow.nodes:
            if node.id == next_node_id:
                next_node = node
                break
        else:
            raise ValueError(f"Node with ID {next_node_id} not found in workflow")
        
        if next_node.type == "GenericNode":
            assert isinstance(next_node, GenericNode)
            generic_node = next_node
            next_node_id, context = await RunGenericNode(generic_node, context)
        elif next_node.type == "EndNode":
            assert isinstance(next_node, EndNode)
            end_node = next_node
            response = await RunEndNode(end_node, context)
            return executeResponse(output=response, chat_history=context.get_messages())
        elif next_node.type == "ConditionalNode":
            assert isinstance(next_node, ConditionalNode)
            conditional_node = next_node
            next_node_id, context = await RunConditionalNode(conditional_node, context)
        else:
            raise ValueError(f"Unknown node type: {next_node.type}")
