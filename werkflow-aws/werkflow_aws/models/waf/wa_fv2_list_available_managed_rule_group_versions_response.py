from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_managed_rule_group_version import WAFv2ManagedRuleGroupVersion


class WAFv2ListAvailableManagedRuleGroupVersionsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    Versions: list[WAFv2ManagedRuleGroupVersion] | None = None
    CurrentDefaultVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
