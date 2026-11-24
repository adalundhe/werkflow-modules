from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetPublicKeyRequest(BaseModel):
    Id: StrictStr
