from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_arc_rule_config import Route53ARCRuleConfig


class Route53ARCGatingRule(BaseModel):
    ControlPanelArn: StrictStr | None = None
    GatingControls: list[StrictStr] | None = None
    Name: StrictStr | None = None
    RuleConfig: Route53ARCRuleConfig | None = None
    SafetyRuleArn: StrictStr | None = None
    Status: StrictStr | None = None
    TargetControls: list[StrictStr] | None = None
    WaitPeriodMs: StrictInt | None = None
    Owner: StrictStr | None = None
