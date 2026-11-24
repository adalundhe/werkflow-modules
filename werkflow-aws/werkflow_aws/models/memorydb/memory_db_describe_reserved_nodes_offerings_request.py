from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBDescribeReservedNodesOfferingsRequest(BaseModel):
    ReservedNodesOfferingId: StrictStr | None = None
    NodeType: StrictStr | None = None
    Duration: StrictStr | None = None
    OfferingType: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
