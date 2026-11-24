from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRuleGroupSourceListDetails(BaseModel):
    GeneratedRulesType: StrictStr | None = None
    TargetTypes: list[StrictStr] | None = None
    Targets: list[StrictStr] | None = None
