from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCreateSpaceRequest(BaseModel):
    AwsAccountId: StrictStr
    SpaceId: StrictStr
    Name: StrictStr
    Description: StrictStr | None = None
