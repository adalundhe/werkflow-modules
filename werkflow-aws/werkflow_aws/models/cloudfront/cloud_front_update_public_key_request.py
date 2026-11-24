from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_public_key_config import CloudFrontPublicKeyConfig


class CloudFrontUpdatePublicKeyRequest(BaseModel):
    PublicKeyConfig: CloudFrontPublicKeyConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
