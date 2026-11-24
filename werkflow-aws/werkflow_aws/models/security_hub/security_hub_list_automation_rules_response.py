from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_automation_rules_metadata import SecurityHubAutomationRulesMetadata


class SecurityHubListAutomationRulesResponse(BaseModel):
    AutomationRulesMetadata: list[SecurityHubAutomationRulesMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
