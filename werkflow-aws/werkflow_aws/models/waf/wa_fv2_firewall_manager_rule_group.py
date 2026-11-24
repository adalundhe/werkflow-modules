from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_firewall_manager_statement import WAFv2FirewallManagerStatement
from .wa_fv2_override_action import WAFv2OverrideAction
from .wa_fv2_visibility_config import WAFv2VisibilityConfig


class WAFv2FirewallManagerRuleGroup(BaseModel):
    Name: StrictStr | None = None
    Priority: StrictInt | None = None
    FirewallManagerStatement: WAFv2FirewallManagerStatement | None = None
    OverrideAction: WAFv2OverrideAction | None = None
    VisibilityConfig: WAFv2VisibilityConfig | None = None
