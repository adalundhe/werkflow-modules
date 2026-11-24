from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeInboundConnectorRequest(BaseModel):
    AwsAccountId: StrictStr
    InboundConnectorId: StrictStr
