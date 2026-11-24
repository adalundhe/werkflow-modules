from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_cost_category_split_charge_rule_parameter import CostExplorerCostCategorySplitChargeRuleParameter


class CostExplorerCostCategorySplitChargeRule(BaseModel):
    Source: StrictStr | None = None
    Targets: list[StrictStr] | None = None
    Method: StrictStr | None = None
    Parameters: list[CostExplorerCostCategorySplitChargeRuleParameter] | None = None
