from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_cached_methods import CloudFrontCachedMethods


class CloudFrontAllowedMethods(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[StrictStr] | None = None
    CachedMethods: CloudFrontCachedMethods | None = None
