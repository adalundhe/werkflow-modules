from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerListCostCategoryResourceAssociationsRequest(BaseModel):
    CostCategoryArn: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
