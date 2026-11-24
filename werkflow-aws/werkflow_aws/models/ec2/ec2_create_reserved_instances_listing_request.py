from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_price_schedule_specification import EC2PriceScheduleSpecification


class EC2CreateReservedInstancesListingRequest(BaseModel):
    ReservedInstancesId: StrictStr
    InstanceCount: StrictInt
    PriceSchedules: list[EC2PriceScheduleSpecification]
    ClientToken: StrictStr
