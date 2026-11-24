from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GuardDutyDetectionRuleFilter(BaseModel):
    Name: Literal['name', 'description', 'dataSource', 'severity', 'tactic', 'technique', 'service']
    Values: list[StrictStr]
    Condition: Literal['EQUALS', 'CONTAINS'] | None = None
