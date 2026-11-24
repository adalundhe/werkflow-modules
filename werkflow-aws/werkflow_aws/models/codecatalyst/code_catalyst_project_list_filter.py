from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeCatalystProjectListFilter(BaseModel):
    key: Literal['hasAccessTo', 'name']
    values: list[StrictStr]
    comparisonOperator: Literal['EQ', 'GT', 'GE', 'LT', 'LE', 'BEGINS_WITH'] | None = None
