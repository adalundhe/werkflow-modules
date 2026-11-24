from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class DetectiveSortCriteria(BaseModel):
    Field: Literal['SEVERITY', 'STATUS', 'CREATED_TIME'] | None = None
    SortOrder: Literal['ASC', 'DESC'] | None = None
