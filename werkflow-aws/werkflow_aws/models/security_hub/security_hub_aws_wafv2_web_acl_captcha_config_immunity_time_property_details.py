from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails(BaseModel):
    ImmunityTime: StrictInt | None = None
