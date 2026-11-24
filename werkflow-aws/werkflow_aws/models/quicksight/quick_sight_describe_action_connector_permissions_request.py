from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeActionConnectorPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    ActionConnectorId: StrictStr
