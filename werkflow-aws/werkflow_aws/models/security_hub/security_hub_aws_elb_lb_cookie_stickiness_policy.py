from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsElbLbCookieStickinessPolicy(BaseModel):
    CookieExpirationPeriod: StrictInt | None = None
    PolicyName: StrictStr | None = None
