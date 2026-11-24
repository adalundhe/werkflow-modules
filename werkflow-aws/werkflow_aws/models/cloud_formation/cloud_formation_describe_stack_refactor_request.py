from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeStackRefactorRequest(BaseModel):
    StackRefactorId: StrictStr
