from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsListExecutionsRequest(BaseModel):
    stateMachineArn: StrictStr | None = None
    statusFilter: Literal['RUNNING', 'SUCCEEDED', 'FAILED', 'TIMED_OUT', 'ABORTED', 'PENDING_REDRIVE'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    mapRunArn: StrictStr | None = None
    redriveFilter: Literal['REDRIVEN', 'NOT_REDRIVEN'] | None = None
