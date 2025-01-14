from pydantic import BaseModel, Field
from typing import Annotated, List, Literal, Union

class StartNode(BaseModel):
    id: str = Field(..., description="Unique identifier for the node")
    type: Literal["StartNode"] = Field("StartNode", description="Indicates this is a start node")
    output: str = Field(..., description="ID of the next node")

class GenericNode(BaseModel):
    id: str = Field(..., description="Unique identifier for the node")
    type: Literal["GenericNode"] = Field("GenericNode", description="Indicates this is a generic node")
    input: str = Field(..., description="ID of the input node")
    output: str = Field(..., description="ID of the next node")
    action: str = Field(..., description="Action to be taken")

class ConditionalOutput(BaseModel):
    value: str = Field(..., description="Condition value")
    output: str = Field(..., description="ID of the corresponding output node")

class ConditionalNode(BaseModel):
    id: str = Field(..., description="Unique identifier for the node")
    type: Literal["ConditionalNode"] = Field("ConditionalNode", description="Indicates this is a conditional node")
    input: str = Field(..., description="ID of the input node")
    condition: str = Field(..., description="Condition to be evaluated")
    outputs: List[ConditionalOutput] = Field(..., description="Array of possible outputs based on conditions")

class EndNode(BaseModel):
    id: str = Field(..., description="Unique identifier for the node")
    type: Literal["EndNode"] = Field("EndNode", description="Indicates this is an end node")
    input: str = Field(..., description="ID of the input node")

Node = Annotated[Union[StartNode, GenericNode, ConditionalNode, EndNode], Field(discriminator="type")]

class AgenticWorkflowSchema(BaseModel):
    nodes: List[Node] = Field(..., description="List of nodes in the workflow")
