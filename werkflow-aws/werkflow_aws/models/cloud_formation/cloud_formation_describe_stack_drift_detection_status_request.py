from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeStackDriftDetectionStatusRequest(BaseModel):
    StackDriftDetectionId: StrictStr
