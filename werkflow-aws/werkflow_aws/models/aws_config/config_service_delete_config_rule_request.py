from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteConfigRuleRequest(BaseModel):
    ConfigRuleName: StrictStr
