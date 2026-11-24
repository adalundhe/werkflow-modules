from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class MacieFindingStatisticsSortCriteria(BaseModel):
    attributeName: Literal['groupKey', 'count'] | None = None
    orderBy: Literal['ASC', 'DESC'] | None = None
