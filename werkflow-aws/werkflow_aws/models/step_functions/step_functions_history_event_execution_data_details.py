from __future__ import annotations
from pydantic import BaseModel, StrictBool


class StepFunctionsHistoryEventExecutionDataDetails(BaseModel):
    truncated: StrictBool | None = None
