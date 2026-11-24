from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteActionConnectorRequest(BaseModel):
    AwsAccountId: StrictStr
    ActionConnectorId: StrictStr
