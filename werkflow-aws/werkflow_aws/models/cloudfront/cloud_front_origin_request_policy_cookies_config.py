from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_cookie_names import CloudFrontCookieNames


class CloudFrontOriginRequestPolicyCookiesConfig(BaseModel):
    CookieBehavior: StrictStr | None = None
    Cookies: CloudFrontCookieNames | None = None
