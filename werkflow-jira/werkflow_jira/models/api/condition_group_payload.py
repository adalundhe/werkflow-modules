from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rule_payload import RulePayload


class ConditionGroupPayload(BaseModel):
    conditionGroup: list[ConditionGroupPayload] | None = None
    conditions: list[RulePayload] | None = None
    operation: StrictStr | None = None
