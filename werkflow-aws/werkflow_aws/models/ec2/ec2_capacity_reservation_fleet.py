from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_fleet_capacity_reservation import EC2FleetCapacityReservation
from .ec2_instance_requirements_request import EC2InstanceRequirementsRequest
from .ec2_tag_model import EC2TagModel


class EC2CapacityReservationFleet(BaseModel):
    CapacityReservationFleetId: StrictStr | None = None
    CapacityReservationFleetArn: StrictStr | None = None
    State: StrictStr | None = None
    TotalTargetCapacity: StrictInt | None = None
    TotalFulfilledCapacity: StrictFloat | StrictInt | None = None
    Tenancy: StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    InstanceMatchCriteria: StrictStr | None = None
    AllocationStrategy: StrictStr | None = None
    InstanceTypeSpecifications: list[EC2FleetCapacityReservation] | None = None
    InstanceRequirements: EC2InstanceRequirementsRequest | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
