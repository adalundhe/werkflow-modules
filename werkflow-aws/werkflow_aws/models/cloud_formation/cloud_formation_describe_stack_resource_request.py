from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeStackResourceRequest(BaseModel):
    StackName: StrictStr
    LogicalResourceId: StrictStr
