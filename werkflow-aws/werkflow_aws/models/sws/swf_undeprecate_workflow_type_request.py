from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_workflow_type import SWFWorkflowType


class SWFUndeprecateWorkflowTypeRequest(BaseModel):
    domain: StrictStr
    workflowType: SWFWorkflowType
