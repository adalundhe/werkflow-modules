from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .cloud_front_cache_policy_cookies_config import CloudFrontCachePolicyCookiesConfig
from .cloud_front_cache_policy_headers_config import CloudFrontCachePolicyHeadersConfig
from .cloud_front_cache_policy_query_strings_config import CloudFrontCachePolicyQueryStringsConfig


class CloudFrontParametersInCacheKeyAndForwardedToOrigin(BaseModel):
    EnableAcceptEncodingGzip: StrictBool | None = None
    EnableAcceptEncodingBrotli: StrictBool | None = None
    HeadersConfig: CloudFrontCachePolicyHeadersConfig | None = None
    CookiesConfig: CloudFrontCachePolicyCookiesConfig | None = None
    QueryStringsConfig: CloudFrontCachePolicyQueryStringsConfig | None = None
