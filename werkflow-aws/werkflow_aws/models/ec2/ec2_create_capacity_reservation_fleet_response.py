from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_fleet_capacity_reservation import EC2FleetCapacityReservation
from .ec2_tag_model import EC2TagModel


class EC2CreateCapacityReservationFleetResponse(BaseModel):
    CapacityReservationFleetId: StrictStr | None = None
    State: StrictStr | None = None
    TotalTargetCapacity: StrictInt | None = None
    TotalFulfilledCapacity: StrictFloat | StrictInt | None = None
    InstanceMatchCriteria: StrictStr | None = None
    AllocationStrategy: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    Tenancy: StrictStr | None = None
    FleetCapacityReservations: list[EC2FleetCapacityReservation] | None = None
    Tags: list[EC2TagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
