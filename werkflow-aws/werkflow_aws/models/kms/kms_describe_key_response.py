from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kms_key_metadata import KMSKeyMetadata


class KMSDescribeKeyResponse(BaseModel):
    KeyMetadata: KMSKeyMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
