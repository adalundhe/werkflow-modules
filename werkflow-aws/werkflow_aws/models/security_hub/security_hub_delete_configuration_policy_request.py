from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteConfigurationPolicyRequest(BaseModel):
    Identifier: StrictStr
