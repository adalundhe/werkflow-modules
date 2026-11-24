from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheDescribeReservedCacheNodesOfferingsRequest(BaseModel):
    ReservedCacheNodesOfferingId: StrictStr | None = None
    CacheNodeType: StrictStr | None = None
    Duration: StrictStr | None = None
    ProductDescription: StrictStr | None = None
    OfferingType: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
