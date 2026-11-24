from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAccountSettingsRequest(BaseModel):
    AwsAccountId: StrictStr
