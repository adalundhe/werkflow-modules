from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from typing import Any


class CostExplorerCostCategoryReference(BaseModel):
    CostCategoryArn: StrictStr | None = None
    Name: StrictStr | None = None
    EffectiveStart: StrictStr | None = None
    EffectiveEnd: StrictStr | None = None
    NumberOfRules: StrictInt | None = None
    ProcessingStatus: list[dict[str, Any]] | None = None
    Values: list[StrictStr] | None = None
    DefaultValue: StrictStr | None = None
