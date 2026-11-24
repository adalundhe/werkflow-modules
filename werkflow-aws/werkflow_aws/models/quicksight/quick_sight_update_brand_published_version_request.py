from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateBrandPublishedVersionRequest(BaseModel):
    AwsAccountId: StrictStr
    BrandId: StrictStr
    VersionId: StrictStr
