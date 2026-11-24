from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GuardDutySortCriteria(BaseModel):
    AttributeName: StrictStr | None = None
    OrderBy: Literal['ASC', 'DESC'] | None = None
