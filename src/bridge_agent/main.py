from fastapi import FastAPI

from bridge_agent.models.workflow import AgenticWorkflowSchema
from bridge_agent.executor import RunWorkflow

app = FastAPI()

@app.post("/execute")
async def execute(workflow: AgenticWorkflowSchema):
    return await RunWorkflow(workflow)
