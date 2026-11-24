from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KendraExpandConfiguration(BaseModel):
    MaxResultItemsToExpand: StrictInt | None = None
    MaxExpandedResultsPerItem: StrictInt | None = None
