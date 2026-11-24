from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cost_explorer_cost_category import CostExplorerCostCategory


class CostExplorerDescribeCostCategoryDefinitionResponse(BaseModel):
    CostCategory: CostExplorerCostCategory | None = None
    ResponseMetadata: dict[str, Any] | None = None
