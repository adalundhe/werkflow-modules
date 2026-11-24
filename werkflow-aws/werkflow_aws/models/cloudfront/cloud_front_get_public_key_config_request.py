from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetPublicKeyConfigRequest(BaseModel):
    Id: StrictStr
