from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_object_lock_configuration import AWSS3ObjectLockConfiguration


class AWSS3GetObjectLockConfigurationResponse(BaseModel):
    ObjectLockConfiguration: AWSS3ObjectLockConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
