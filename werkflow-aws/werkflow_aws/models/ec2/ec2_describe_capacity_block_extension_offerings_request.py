from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeCapacityBlockExtensionOfferingsRequest(BaseModel):
    CapacityBlockExtensionDurationHours: StrictInt
    CapacityReservationId: StrictStr
    DryRun: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
