from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationExecuteStackRefactorRequest(BaseModel):
    StackRefactorId: StrictStr
