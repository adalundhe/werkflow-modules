from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_cost_category_reference import CostExplorerCostCategoryReference


class CostExplorerListCostCategoryDefinitionsResponse(BaseModel):
    CostCategoryReferences: list[CostExplorerCostCategoryReference] | None = None
    NextToken: StrictStr | None = None
