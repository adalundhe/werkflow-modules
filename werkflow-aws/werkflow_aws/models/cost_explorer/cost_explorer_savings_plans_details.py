from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerSavingsPlansDetails(BaseModel):
    Region: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    OfferingId: StrictStr | None = None
