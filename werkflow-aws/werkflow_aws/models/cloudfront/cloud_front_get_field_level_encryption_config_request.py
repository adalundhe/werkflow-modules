from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetFieldLevelEncryptionConfigRequest(BaseModel):
    Id: StrictStr
