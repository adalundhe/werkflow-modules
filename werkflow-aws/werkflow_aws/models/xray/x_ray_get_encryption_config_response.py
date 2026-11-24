from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .x_ray_encryption_config import XRayEncryptionConfig


class XRayGetEncryptionConfigResponse(BaseModel):
    EncryptionConfig: XRayEncryptionConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
