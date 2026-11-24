from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSNetworkFirewallStatefulRuleGroupOverride(BaseModel):
    Action: StrictStr | None = None
