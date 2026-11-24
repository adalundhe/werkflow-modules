from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubCreateAutomationRuleV2Response(BaseModel):
    RuleArn: StrictStr | None = None
    RuleId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
