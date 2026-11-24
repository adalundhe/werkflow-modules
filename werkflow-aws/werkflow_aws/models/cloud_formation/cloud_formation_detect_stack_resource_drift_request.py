from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDetectStackResourceDriftRequest(BaseModel):
    StackName: StrictStr
    LogicalResourceId: StrictStr
