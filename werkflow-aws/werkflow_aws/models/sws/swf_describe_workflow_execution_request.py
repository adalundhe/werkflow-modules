from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_workflow_execution import SWFWorkflowExecution


class SWFDescribeWorkflowExecutionRequest(BaseModel):
    domain: StrictStr
    execution: SWFWorkflowExecution
