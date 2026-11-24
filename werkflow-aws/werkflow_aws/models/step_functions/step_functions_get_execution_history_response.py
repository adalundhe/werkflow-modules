from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .step_functions_history_event import StepFunctionsHistoryEvent


class StepFunctionsGetExecutionHistoryResponse(BaseModel):
    events: list[StepFunctionsHistoryEvent] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
