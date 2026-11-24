from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QuickSightPaginationConfiguration(BaseModel):
    PageSize: StrictInt | None = None
    PageNumber: StrictInt | None = None
