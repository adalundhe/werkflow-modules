from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeActionConnectorRequest(BaseModel):
    AwsAccountId: StrictStr
    ActionConnectorId: StrictStr
