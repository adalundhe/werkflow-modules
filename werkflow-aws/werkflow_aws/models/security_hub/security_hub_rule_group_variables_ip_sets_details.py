from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRuleGroupVariablesIpSetsDetails(BaseModel):
    Definition: list[StrictStr] | None = None
