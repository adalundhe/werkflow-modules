from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerMetricValue(BaseModel):
    Amount: StrictStr | None = None
    Unit: StrictStr | None = None
