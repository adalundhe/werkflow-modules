from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_managed_rule_set import WAFv2ManagedRuleSet


class WAFv2GetManagedRuleSetResponse(BaseModel):
    ManagedRuleSet: WAFv2ManagedRuleSet | None = None
    LockToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
