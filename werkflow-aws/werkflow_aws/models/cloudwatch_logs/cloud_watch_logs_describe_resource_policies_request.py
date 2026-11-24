from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeResourcePoliciesRequest(BaseModel):
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    resourceArn: StrictStr | None = None
    policyScope: Literal['ACCOUNT', 'RESOURCE'] | None = None
