from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsDeleteStateMachineRequest(BaseModel):
    stateMachineArn: StrictStr
