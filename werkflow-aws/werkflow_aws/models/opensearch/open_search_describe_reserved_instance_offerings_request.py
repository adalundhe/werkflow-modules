from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchDescribeReservedInstanceOfferingsRequest(BaseModel):
    ReservedInstanceOfferingId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
