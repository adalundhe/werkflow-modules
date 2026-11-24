from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_parameters_in_cache_key_and_forwarded_to_origin import CloudFrontParametersInCacheKeyAndForwardedToOrigin


class CloudFrontCachePolicyConfig(BaseModel):
    Comment: StrictStr | None = None
    Name: StrictStr | None = None
    DefaultTTL: StrictInt | None = None
    MaxTTL: StrictInt | None = None
    MinTTL: StrictInt | None = None
    ParametersInCacheKeyAndForwardedToOrigin: CloudFrontParametersInCacheKeyAndForwardedToOrigin | None = None
