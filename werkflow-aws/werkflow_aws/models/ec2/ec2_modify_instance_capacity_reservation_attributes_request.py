from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_capacity_reservation_specification import EC2CapacityReservationSpecification


class EC2ModifyInstanceCapacityReservationAttributesRequest(BaseModel):
    InstanceId: StrictStr
    CapacityReservationSpecification: EC2CapacityReservationSpecification
    DryRun: StrictBool | None = None
