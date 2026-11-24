from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_object_lock_retention import AWSS3ObjectLockRetention


class AWSS3GetObjectRetentionResponse(BaseModel):
    Retention: AWSS3ObjectLockRetention | None = None
    ResponseMetadata: dict[str, Any] | None = None
