from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteSpaceRequest(BaseModel):
    AwsAccountId: StrictStr
    SpaceId: StrictStr
