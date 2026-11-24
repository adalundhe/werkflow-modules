from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRuleGroupSourceStatelessRuleMatchAttributesTcpFlags(BaseModel):
    Flags: list[StrictStr] | None = None
    Masks: list[StrictStr] | None = None
