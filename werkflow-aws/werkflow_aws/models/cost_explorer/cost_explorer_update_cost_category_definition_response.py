from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CostExplorerUpdateCostCategoryDefinitionResponse(BaseModel):
    CostCategoryArn: StrictStr | None = None
    EffectiveStart: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
