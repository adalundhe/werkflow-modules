from __future__ import annotations
from pydantic import BaseModel, StrictBool


class StepFunctionsTracingConfiguration(BaseModel):
    enabled: StrictBool | None = None
