from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftPurchaseReservedNodeOfferingRequest(BaseModel):
    ReservedNodeOfferingId: StrictStr
    NodeCount: StrictInt | None = None
