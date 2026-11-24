from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class GlueTaskRunSortCriteria(BaseModel):
    Column: Literal['TASK_RUN_TYPE', 'STATUS', 'STARTED']
    SortDirection: Literal['DESCENDING', 'ASCENDING']
