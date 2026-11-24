from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeBrandPublishedVersionRequest(BaseModel):
    AwsAccountId: StrictStr
    BrandId: StrictStr
