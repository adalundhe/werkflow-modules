from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_cost_category_values import CostExplorerCostCategoryValues
from .cost_explorer_dimension_values import CostExplorerDimensionValues
from .cost_explorer_product_attribute_values import CostExplorerProductAttributeValues
from .cost_explorer_tag_values import CostExplorerTagValues


class CostExplorerExpression(BaseModel):
    Or: list[CostExplorerExpression] | None = None
    And: list[CostExplorerExpression] | None = None
    Not: CostExplorerExpression | None = None
    Dimensions: CostExplorerDimensionValues | None = None
    Tags: CostExplorerTagValues | None = None
    CostCategories: CostExplorerCostCategoryValues | None = None
    ProductAttributes: CostExplorerProductAttributeValues | None = None
