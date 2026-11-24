from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetConfigurationPolicyRequest(BaseModel):
    Identifier: StrictStr
