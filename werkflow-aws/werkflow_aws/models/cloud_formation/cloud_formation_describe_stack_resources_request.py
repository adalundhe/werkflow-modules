from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeStackResourcesRequest(BaseModel):
    StackName: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
