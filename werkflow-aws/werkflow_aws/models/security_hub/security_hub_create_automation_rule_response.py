from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubCreateAutomationRuleResponse(BaseModel):
    RuleArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
