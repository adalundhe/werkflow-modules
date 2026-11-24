from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueSortCriterion(BaseModel):
    FieldName: StrictStr | None = None
    Sort: Literal['ASC', 'DESC'] | None = None
