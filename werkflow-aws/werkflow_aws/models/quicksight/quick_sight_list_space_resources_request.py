from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightListSpaceResourcesRequest(BaseModel):
    AwsAccountId: StrictStr
    SpaceId: StrictStr
