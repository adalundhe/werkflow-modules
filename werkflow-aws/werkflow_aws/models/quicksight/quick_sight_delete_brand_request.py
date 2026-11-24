from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteBrandRequest(BaseModel):
    AwsAccountId: StrictStr
    BrandId: StrictStr
