from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCostCategoryValues(BaseModel):
    Key: StrictStr | None = None
    Values: list[StrictStr] | None = None
    MatchOptions: list[StrictStr] | None = None
