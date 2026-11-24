from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerDescribeCostCategoryDefinitionRequest(BaseModel):
    CostCategoryArn: StrictStr
    EffectiveOn: StrictStr | None = None
