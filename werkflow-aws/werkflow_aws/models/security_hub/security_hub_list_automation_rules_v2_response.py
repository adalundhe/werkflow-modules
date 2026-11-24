from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_automation_rules_metadata_v2 import SecurityHubAutomationRulesMetadataV2


class SecurityHubListAutomationRulesV2Response(BaseModel):
    Rules: list[SecurityHubAutomationRulesMetadataV2] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
