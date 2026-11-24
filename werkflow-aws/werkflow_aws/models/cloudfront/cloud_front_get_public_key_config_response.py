from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_public_key_config import CloudFrontPublicKeyConfig


class CloudFrontGetPublicKeyConfigResponse(BaseModel):
    PublicKeyConfig: CloudFrontPublicKeyConfig | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
