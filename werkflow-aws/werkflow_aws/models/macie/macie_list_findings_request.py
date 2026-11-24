from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_finding_criteria import MacieFindingCriteria
from .macie_sort_criteria import MacieSortCriteria


class MacieListFindingsRequest(BaseModel):
    findingCriteria: MacieFindingCriteria | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortCriteria: MacieSortCriteria | None = None
