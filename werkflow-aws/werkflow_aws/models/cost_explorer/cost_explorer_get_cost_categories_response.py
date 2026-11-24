from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerGetCostCategoriesResponse(BaseModel):
    NextPageToken: StrictStr | None = None
    CostCategoryNames: list[StrictStr] | None = None
    CostCategoryValues: list[StrictStr] | None = None
    ReturnSize: StrictInt | None = None
    TotalSize: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
