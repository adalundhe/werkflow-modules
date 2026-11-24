from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerAnomalyDateInterval(BaseModel):
    StartDate: StrictStr
    EndDate: StrictStr | None = None
