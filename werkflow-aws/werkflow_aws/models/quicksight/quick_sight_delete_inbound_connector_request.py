from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteInboundConnectorRequest(BaseModel):
    AwsAccountId: StrictStr
    InboundConnectorId: StrictStr
