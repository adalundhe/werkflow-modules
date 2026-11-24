from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieBucketSortCriteria(BaseModel):
    attributeName: StrictStr | None = None
    orderBy: Literal['ASC', 'DESC'] | None = None
