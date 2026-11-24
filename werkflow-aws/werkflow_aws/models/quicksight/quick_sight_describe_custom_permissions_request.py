from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeCustomPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    CustomPermissionsName: StrictStr
