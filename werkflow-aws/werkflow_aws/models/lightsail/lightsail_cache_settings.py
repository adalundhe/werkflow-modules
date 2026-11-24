from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_cookie_object import LightsailCookieObject
from .lightsail_header_object import LightsailHeaderObject
from .lightsail_query_string_object import LightsailQueryStringObject


class LightsailCacheSettings(BaseModel):
    defaultTTL: StrictInt | None = None
    minimumTTL: StrictInt | None = None
    maximumTTL: StrictInt | None = None
    allowedHTTPMethods: StrictStr | None = None
    cachedHTTPMethods: StrictStr | None = None
    forwardedCookies: LightsailCookieObject | None = None
    forwardedHeaders: LightsailHeaderObject | None = None
    forwardedQueryStrings: LightsailQueryStringObject | None = None
