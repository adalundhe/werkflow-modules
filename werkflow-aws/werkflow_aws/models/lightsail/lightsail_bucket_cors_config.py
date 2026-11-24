from __future__ import annotations
from pydantic import BaseModel
from .lightsail_bucket_cors_rule import LightsailBucketCorsRule


class LightsailBucketCorsConfig(BaseModel):
    rules: list[LightsailBucketCorsRule] | None = None
