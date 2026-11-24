from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDetectStackDriftRequest(BaseModel):
    StackName: StrictStr
    LogicalResourceIds: list[StrictStr] | None = None
