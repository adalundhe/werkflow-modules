from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRuleGroupVariablesPortSetsDetails(BaseModel):
    Definition: list[StrictStr] | None = None
