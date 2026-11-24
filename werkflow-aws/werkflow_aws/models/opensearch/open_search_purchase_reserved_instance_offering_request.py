from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchPurchaseReservedInstanceOfferingRequest(BaseModel):
    ReservedInstanceOfferingId: StrictStr
    ReservationName: StrictStr
    InstanceCount: StrictInt | None = None
