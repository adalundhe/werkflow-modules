from __future__ import annotations
from pydantic import BaseModel
from .connect_rule_attribute_filter import ConnectRuleAttributeFilter


class ConnectRulesSearchFilter(BaseModel):
    AttributeFilter: ConnectRuleAttributeFilter | None = None
