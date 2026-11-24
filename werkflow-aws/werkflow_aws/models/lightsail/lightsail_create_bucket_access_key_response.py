from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_access_key import LightsailAccessKey
from .lightsail_operation import LightsailOperation


class LightsailCreateBucketAccessKeyResponse(BaseModel):
    accessKey: LightsailAccessKey | None = None
    operations: list[LightsailOperation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
