from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .swf_workflow_execution import SWFWorkflowExecution


class SWFGetWorkflowExecutionHistoryRequest(BaseModel):
    domain: StrictStr
    execution: SWFWorkflowExecution
    nextPageToken: StrictStr | None = None
    maximumPageSize: StrictInt | None = None
    reverseOrder: StrictBool | None = None
