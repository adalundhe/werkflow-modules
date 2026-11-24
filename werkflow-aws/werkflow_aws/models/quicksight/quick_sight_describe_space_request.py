from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDescribeSpaceRequest(BaseModel):
    AwsAccountId: StrictStr
    SpaceId: StrictStr
    MaxContributors: StrictInt | None = None
