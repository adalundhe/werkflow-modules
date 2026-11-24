from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeResourcePermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
