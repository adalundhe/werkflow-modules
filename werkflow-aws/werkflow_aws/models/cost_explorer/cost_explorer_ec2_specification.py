from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerEC2Specification(BaseModel):
    OfferingClass: StrictStr | None = None
