from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_cookie_names import CloudFrontCookieNames


class CloudFrontCookiePreference(BaseModel):
    Forward: StrictStr | None = None
    WhitelistedNames: CloudFrontCookieNames | None = None
