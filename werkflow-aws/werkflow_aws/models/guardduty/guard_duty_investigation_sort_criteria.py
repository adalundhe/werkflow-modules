from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class GuardDutyInvestigationSortCriteria(BaseModel):
    AttributeName: Literal['START_TIME', 'END_TIME', 'STATUS', 'RISK_LEVEL', 'CONFIDENCE'] | None = None
    OrderBy: Literal['ASC', 'DESC'] | None = None
