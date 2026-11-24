from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeResiliencyPolicyRequest(BaseModel):
    policyArn: StrictStr
