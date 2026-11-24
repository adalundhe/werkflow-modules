from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SecurityHubSortCriterion(BaseModel):
    Field: StrictStr | None = None
    SortOrder: Literal['asc', 'desc'] | None = None
