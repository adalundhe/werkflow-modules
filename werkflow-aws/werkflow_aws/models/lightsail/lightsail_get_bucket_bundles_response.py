from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_bucket_bundle import LightsailBucketBundle


class LightsailGetBucketBundlesResponse(BaseModel):
    bundles: list[LightsailBucketBundle] | None = None
    ResponseMetadata: dict[str, Any] | None = None
