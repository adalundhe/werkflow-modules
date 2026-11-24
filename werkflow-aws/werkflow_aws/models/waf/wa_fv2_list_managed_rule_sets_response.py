from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_managed_rule_set_summary import WAFv2ManagedRuleSetSummary


class WAFv2ListManagedRuleSetsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    ManagedRuleSets: list[WAFv2ManagedRuleSetSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
