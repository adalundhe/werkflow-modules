from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lightsail_waf_rule import LightsailWafRule


class LightsailWafConfig(BaseModel):
    isWafEnabled: StrictBool | None = None
    wafRules: list[LightsailWafRule] | None = None
