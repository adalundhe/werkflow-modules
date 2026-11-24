from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .memory_db_recurring_charge import MemoryDBRecurringCharge


class MemoryDBReservedNode(BaseModel):
    ReservationId: StrictStr | None = None
    ReservedNodesOfferingId: StrictStr | None = None
    NodeType: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    NodeCount: StrictInt | None = None
    OfferingType: StrictStr | None = None
    State: StrictStr | None = None
    RecurringCharges: list[MemoryDBRecurringCharge] | None = None
    ARN: StrictStr | None = None
