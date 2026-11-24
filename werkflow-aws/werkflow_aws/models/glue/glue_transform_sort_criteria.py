from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class GlueTransformSortCriteria(BaseModel):
    Column: Literal['NAME', 'TRANSFORM_TYPE', 'STATUS', 'CREATED', 'LAST_MODIFIED']
    SortDirection: Literal['DESCENDING', 'ASCENDING']
