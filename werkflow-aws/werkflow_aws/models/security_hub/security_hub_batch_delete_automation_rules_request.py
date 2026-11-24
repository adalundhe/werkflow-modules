from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubBatchDeleteAutomationRulesRequest(BaseModel):
    AutomationRulesArns: list[StrictStr]
