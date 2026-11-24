from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_public_key_list import CloudFrontPublicKeyList


class CloudFrontListPublicKeysResponse(BaseModel):
    PublicKeyList: CloudFrontPublicKeyList | None = None
    ResponseMetadata: dict[str, Any] | None = None
