from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_instance_requirements_request import EC2InstanceRequirementsRequest
from .ec2_reservation_fleet_instance_specification import EC2ReservationFleetInstanceSpecification
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateCapacityReservationFleetRequest(BaseModel):
    TotalTargetCapacity: StrictInt
    AllocationStrategy: StrictStr | None = None
    ClientToken: StrictStr | None = None
    InstanceTypeSpecifications: list[EC2ReservationFleetInstanceSpecification] | None = None
    InstanceRequirements: EC2InstanceRequirementsRequest | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Tenancy: Literal['default'] | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    InstanceMatchCriteria: Literal['open'] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
