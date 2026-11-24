from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeSpacePermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    SpaceId: StrictStr
