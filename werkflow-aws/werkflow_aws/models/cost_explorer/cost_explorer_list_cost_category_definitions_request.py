from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerListCostCategoryDefinitionsRequest(BaseModel):
    EffectiveOn: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
