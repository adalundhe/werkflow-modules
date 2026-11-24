from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SWFTerminateWorkflowExecutionRequest(BaseModel):
    domain: StrictStr
    workflowId: StrictStr
    runId: StrictStr | None = None
    reason: StrictStr | None = None
    details: StrictStr | None = None
    childPolicy: Literal['TERMINATE', 'REQUEST_CANCEL', 'ABANDON'] | None = None
