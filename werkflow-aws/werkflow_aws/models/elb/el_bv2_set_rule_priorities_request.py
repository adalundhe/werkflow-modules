from __future__ import annotations
from pydantic import BaseModel
from .el_bv2_rule_priority_pair import ELBv2RulePriorityPair


class ELBv2SetRulePrioritiesRequest(BaseModel):
    RulePriorities: list[ELBv2RulePriorityPair]
