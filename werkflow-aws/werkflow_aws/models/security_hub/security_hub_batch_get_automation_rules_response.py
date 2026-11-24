from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_automation_rules_config import SecurityHubAutomationRulesConfig
from .security_hub_unprocessed_automation_rule import SecurityHubUnprocessedAutomationRule


class SecurityHubBatchGetAutomationRulesResponse(BaseModel):
    Rules: list[SecurityHubAutomationRulesConfig] | None = None
    UnprocessedAutomationRules: list[SecurityHubUnprocessedAutomationRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
