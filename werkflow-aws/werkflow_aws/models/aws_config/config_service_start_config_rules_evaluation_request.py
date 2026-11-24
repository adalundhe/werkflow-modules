from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceStartConfigRulesEvaluationRequest(BaseModel):
    ConfigRuleNames: list[StrictStr] | None = None
