from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .memory_db_recurring_charge import MemoryDBRecurringCharge


class MemoryDBReservedNodesOffering(BaseModel):
    ReservedNodesOfferingId: StrictStr | None = None
    NodeType: StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    OfferingType: StrictStr | None = None
    RecurringCharges: list[MemoryDBRecurringCharge] | None = None
