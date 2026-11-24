from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_cost_category_processing_status import CostExplorerCostCategoryProcessingStatus
from .cost_explorer_cost_category_rule import CostExplorerCostCategoryRule
from .cost_explorer_cost_category_split_charge_rule import CostExplorerCostCategorySplitChargeRule


class CostExplorerCostCategory(BaseModel):
    CostCategoryArn: StrictStr | None = None
    EffectiveStart: StrictStr | None = None
    EffectiveEnd: StrictStr | None = None
    Name: StrictStr | None = None
    RuleVersion: StrictStr | None = None
    Rules: list[CostExplorerCostCategoryRule] | None = None
    SplitChargeRules: list[CostExplorerCostCategorySplitChargeRule] | None = None
    ProcessingStatus: list[CostExplorerCostCategoryProcessingStatus] | None = None
    DefaultValue: StrictStr | None = None
