from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .preview_rule_configuration import PreviewRuleConfiguration


class PreviewConditionGroupConfiguration(BaseModel):
    conditionGroups: list[PreviewConditionGroupConfiguration] | None = None
    conditions: list[PreviewRuleConfiguration] | None = None
    operation: StrictStr | None = None
