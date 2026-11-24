from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_unprocessed_automation_rule import SecurityHubUnprocessedAutomationRule


class SecurityHubBatchUpdateAutomationRulesResponse(BaseModel):
    ProcessedAutomationRules: list[StrictStr] | None = None
    UnprocessedAutomationRules: list[SecurityHubUnprocessedAutomationRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
