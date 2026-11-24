from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_bucket import LightsailBucket
from .lightsail_operation import LightsailOperation


class LightsailCreateBucketResponse(BaseModel):
    bucket: LightsailBucket | None = None
    operations: list[LightsailOperation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
