from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsDescribeStateMachineAliasRequest(BaseModel):
    stateMachineAliasArn: StrictStr
