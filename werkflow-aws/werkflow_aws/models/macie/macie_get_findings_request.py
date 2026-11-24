from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_sort_criteria import MacieSortCriteria


class MacieGetFindingsRequest(BaseModel):
    findingIds: list[StrictStr]
    sortCriteria: MacieSortCriteria | None = None
