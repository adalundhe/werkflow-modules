from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteTrustStoreRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
