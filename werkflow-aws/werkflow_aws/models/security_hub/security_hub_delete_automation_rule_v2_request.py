from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteAutomationRuleV2Request(BaseModel):
    Identifier: StrictStr
