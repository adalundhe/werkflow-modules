from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeBrandRequest(BaseModel):
    AwsAccountId: StrictStr
    BrandId: StrictStr
    VersionId: StrictStr | None = None
