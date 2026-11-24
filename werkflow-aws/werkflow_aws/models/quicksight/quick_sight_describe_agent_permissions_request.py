from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAgentPermissionsRequest(BaseModel):
    AgentId: StrictStr
    AwsAccountId: StrictStr
