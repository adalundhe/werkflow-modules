from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateSpaceRequest(BaseModel):
    AwsAccountId: StrictStr
    SpaceId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
