from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeHostReservationsRequest(BaseModel):
    Filter: list[EC2FilterModel] | None = None
    HostReservationIdSet: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
