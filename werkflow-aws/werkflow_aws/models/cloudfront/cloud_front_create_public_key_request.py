from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_public_key_config import CloudFrontPublicKeyConfig


class CloudFrontCreatePublicKeyRequest(BaseModel):
    PublicKeyConfig: CloudFrontPublicKeyConfig
