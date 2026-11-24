from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_public_key import CloudFrontPublicKey


class CloudFrontUpdatePublicKeyResponse(BaseModel):
    PublicKey: CloudFrontPublicKey | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
