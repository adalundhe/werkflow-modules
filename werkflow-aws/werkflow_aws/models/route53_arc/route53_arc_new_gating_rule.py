from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_arc_rule_config import Route53ARCRuleConfig


class Route53ARCNewGatingRule(BaseModel):
    ControlPanelArn: StrictStr
    GatingControls: list[StrictStr]
    Name: StrictStr
    RuleConfig: Route53ARCRuleConfig
    TargetControls: list[StrictStr]
    WaitPeriodMs: StrictInt
