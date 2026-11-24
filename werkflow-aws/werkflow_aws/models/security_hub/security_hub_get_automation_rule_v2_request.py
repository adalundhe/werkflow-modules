from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetAutomationRuleV2Request(BaseModel):
    Identifier: StrictStr
