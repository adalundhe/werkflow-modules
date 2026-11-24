from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerDimensionValuesWithAttributes(BaseModel):
    Value: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
