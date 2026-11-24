from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .elasti_cache_recurring_charge import ElastiCacheRecurringCharge


class ElastiCacheReservedCacheNodesOffering(BaseModel):
    ReservedCacheNodesOfferingId: StrictStr | None = None
    CacheNodeType: StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    ProductDescription: StrictStr | None = None
    OfferingType: StrictStr | None = None
    RecurringCharges: list[ElastiCacheRecurringCharge] | None = None
