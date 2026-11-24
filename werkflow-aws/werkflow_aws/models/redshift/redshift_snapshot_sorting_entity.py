from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class RedshiftSnapshotSortingEntity(BaseModel):
    Attribute: Literal['SOURCE_TYPE', 'TOTAL_SIZE', 'CREATE_TIME']
    SortOrder: Literal['ASC', 'DESC'] | None = None
