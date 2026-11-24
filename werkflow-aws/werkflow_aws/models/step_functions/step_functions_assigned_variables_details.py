from __future__ import annotations
from pydantic import BaseModel, StrictBool


class StepFunctionsAssignedVariablesDetails(BaseModel):
    truncated: StrictBool | None = None
