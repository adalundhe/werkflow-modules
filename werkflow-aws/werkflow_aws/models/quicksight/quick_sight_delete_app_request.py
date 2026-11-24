from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteAppRequest(BaseModel):
    AwsAccountId: StrictStr
    AppId: StrictStr
