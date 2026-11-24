from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_cost_category_resource_association import CostExplorerCostCategoryResourceAssociation


class CostExplorerListCostCategoryResourceAssociationsResponse(BaseModel):
    CostCategoryResourceAssociations: list[CostExplorerCostCategoryResourceAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
