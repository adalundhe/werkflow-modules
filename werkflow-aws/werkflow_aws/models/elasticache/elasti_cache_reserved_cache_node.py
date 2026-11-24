from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .elasti_cache_recurring_charge import ElastiCacheRecurringCharge


class ElastiCacheReservedCacheNode(BaseModel):
    ReservedCacheNodeId: StrictStr | None = None
    ReservedCacheNodesOfferingId: StrictStr | None = None
    CacheNodeType: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    CacheNodeCount: StrictInt | None = None
    ProductDescription: StrictStr | None = None
    OfferingType: StrictStr | None = None
    State: StrictStr | None = None
    RecurringCharges: list[ElastiCacheRecurringCharge] | None = None
    ReservationARN: StrictStr | None = None
