from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CostExplorerDeleteCostCategoryDefinitionResponse(BaseModel):
    CostCategoryArn: StrictStr | None = None
    EffectiveEnd: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
