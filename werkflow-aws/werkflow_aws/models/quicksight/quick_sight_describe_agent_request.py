from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAgentRequest(BaseModel):
    AgentId: StrictStr
    AwsAccountId: StrictStr
