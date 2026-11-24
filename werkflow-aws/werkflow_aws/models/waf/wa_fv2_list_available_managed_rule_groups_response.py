from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_managed_rule_group_summary import WAFv2ManagedRuleGroupSummary


class WAFv2ListAvailableManagedRuleGroupsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    ManagedRuleGroups: list[WAFv2ManagedRuleGroupSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
