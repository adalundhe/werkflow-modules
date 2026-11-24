from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_cost_category_inherited_value_dimension import CostExplorerCostCategoryInheritedValueDimension
from .cost_explorer_expression import CostExplorerExpression


class CostExplorerCostCategoryRule(BaseModel):
    Value: StrictStr | None = None
    Rule: CostExplorerExpression | None = None
    InheritedValue: CostExplorerCostCategoryInheritedValueDimension | None = None
    Type: StrictStr | None = None
