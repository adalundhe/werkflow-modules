from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeCapacityReservationBillingRequestsRequest(BaseModel):
    Role: Literal['odcr-owner', 'unused-reservation-billing-owner']
    CapacityReservationIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filters: list[EC2FilterModel] | None = None
    DryRun: StrictBool | None = None
