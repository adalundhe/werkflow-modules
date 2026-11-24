from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_cache_behavior import CloudFrontCacheBehavior


class CloudFrontCacheBehaviors(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontCacheBehavior] | None = None
