from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AvailableWorkflowSystemRule(BaseModel):
    description: StrictStr | None = None
    incompatibleRuleKeys: list[StrictStr] | None = None
    isAvailableForInitialTransition: StrictBool | None = None
    isVisible: StrictBool | None = None
    name: StrictStr | None = None
    ruleKey: StrictStr | None = None
    ruleType: StrictStr | None = None
