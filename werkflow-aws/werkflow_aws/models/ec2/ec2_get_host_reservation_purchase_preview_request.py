from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2GetHostReservationPurchasePreviewRequest(BaseModel):
    HostIdSet: list[StrictStr]
    OfferingId: StrictStr
