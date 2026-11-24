from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_arc_rule_config import Route53ARCRuleConfig


class Route53ARCNewAssertionRule(BaseModel):
    AssertedControls: list[StrictStr]
    ControlPanelArn: StrictStr
    Name: StrictStr
    RuleConfig: Route53ARCRuleConfig
    WaitPeriodMs: StrictInt
