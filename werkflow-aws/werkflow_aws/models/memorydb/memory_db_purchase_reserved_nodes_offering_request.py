from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBPurchaseReservedNodesOfferingRequest(BaseModel):
    ReservedNodesOfferingId: StrictStr
    ReservationId: StrictStr | None = None
    NodeCount: StrictInt | None = None
    Tags: list[MemoryDBTag] | None = None
