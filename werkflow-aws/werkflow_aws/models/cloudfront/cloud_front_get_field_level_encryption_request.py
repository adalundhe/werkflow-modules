from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetFieldLevelEncryptionRequest(BaseModel):
    Id: StrictStr
