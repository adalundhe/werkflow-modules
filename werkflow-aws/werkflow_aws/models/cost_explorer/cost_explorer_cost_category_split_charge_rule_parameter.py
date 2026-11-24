from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCostCategorySplitChargeRuleParameter(BaseModel):
    Type: StrictStr | None = None
    Values: list[StrictStr] | None = None
