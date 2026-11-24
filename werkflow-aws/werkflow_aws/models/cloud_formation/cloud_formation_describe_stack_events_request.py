from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeStackEventsRequest(BaseModel):
    StackName: StrictStr
    NextToken: StrictStr | None = None
