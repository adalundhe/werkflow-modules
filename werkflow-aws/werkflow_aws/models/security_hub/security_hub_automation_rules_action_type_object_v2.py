from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAutomationRulesActionTypeObjectV2(BaseModel):
    Type: StrictStr | None = None
