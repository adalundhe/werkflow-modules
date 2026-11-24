from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerProductAttributeValues(BaseModel):
    Key: StrictStr | None = None
    Values: list[StrictStr] | None = None
    MatchOptions: list[StrictStr] | None = None
