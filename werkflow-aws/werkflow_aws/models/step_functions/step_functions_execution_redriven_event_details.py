from __future__ import annotations
from pydantic import BaseModel, StrictInt


class StepFunctionsExecutionRedrivenEventDetails(BaseModel):
    redriveCount: StrictInt | None = None
