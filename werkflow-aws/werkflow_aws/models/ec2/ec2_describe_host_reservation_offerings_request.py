from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeHostReservationOfferingsRequest(BaseModel):
    Filter: list[EC2FilterModel] | None = None
    MaxDuration: StrictInt | None = None
    MaxResults: StrictInt | None = None
    MinDuration: StrictInt | None = None
    NextToken: StrictStr | None = None
    OfferingId: StrictStr | None = None
