from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_stateful_engine_options import FMSStatefulEngineOptions
from .fms_stateful_rule_group import FMSStatefulRuleGroup
from .fms_stateless_rule_group import FMSStatelessRuleGroup


class FMSNetworkFirewallPolicyDescription(BaseModel):
    StatelessRuleGroups: list[FMSStatelessRuleGroup] | None = None
    StatelessDefaultActions: list[StrictStr] | None = None
    StatelessFragmentDefaultActions: list[StrictStr] | None = None
    StatelessCustomActions: list[StrictStr] | None = None
    StatefulRuleGroups: list[FMSStatefulRuleGroup] | None = None
    StatefulDefaultActions: list[StrictStr] | None = None
    StatefulEngineOptions: FMSStatefulEngineOptions | None = None
