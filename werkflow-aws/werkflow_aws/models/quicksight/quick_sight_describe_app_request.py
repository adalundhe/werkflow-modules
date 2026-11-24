from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAppRequest(BaseModel):
    AwsAccountId: StrictStr
    AppId: StrictStr
