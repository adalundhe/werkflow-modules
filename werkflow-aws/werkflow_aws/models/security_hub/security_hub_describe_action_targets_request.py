from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubDescribeActionTargetsRequest(BaseModel):
    ActionTargetArns: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
