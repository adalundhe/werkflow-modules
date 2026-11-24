from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cost_explorer_cost_category_rule import CostExplorerCostCategoryRule
from .cost_explorer_cost_category_split_charge_rule import CostExplorerCostCategorySplitChargeRule
from .cost_explorer_resource_tag import CostExplorerResourceTag


class CostExplorerCreateCostCategoryDefinitionRequest(BaseModel):
    Name: StrictStr
    RuleVersion: Literal['CostCategoryExpression.v1']
    Rules: list[CostExplorerCostCategoryRule]
    EffectiveStart: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    SplitChargeRules: list[CostExplorerCostCategorySplitChargeRule] | None = None
    ResourceTags: list[CostExplorerResourceTag] | None = None
