from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsElbAppCookieStickinessPolicy(BaseModel):
    CookieName: StrictStr | None = None
    PolicyName: StrictStr | None = None
