from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetTrustStoreRequest(BaseModel):
    Identifier: StrictStr
