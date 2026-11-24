from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .cloud_front_cookie_preference import CloudFrontCookiePreference
from .cloud_front_headers import CloudFrontHeaders
from .cloud_front_query_string_cache_keys import CloudFrontQueryStringCacheKeys


class CloudFrontForwardedValues(BaseModel):
    QueryString: StrictBool | None = None
    Cookies: CloudFrontCookiePreference | None = None
    Headers: CloudFrontHeaders | None = None
    QueryStringCacheKeys: CloudFrontQueryStringCacheKeys | None = None
