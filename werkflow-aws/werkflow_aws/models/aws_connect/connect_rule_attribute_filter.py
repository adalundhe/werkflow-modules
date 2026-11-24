from __future__ import annotations
from pydantic import BaseModel
from .connect_rule_attribute_and_condition import ConnectRuleAttributeAndCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectRuleAttributeFilter(BaseModel):
    OrConditions: list[ConnectRuleAttributeAndCondition] | None = None
    AndCondition: ConnectRuleAttributeAndCondition | None = None
    TagCondition: ConnectTagCondition | None = None
