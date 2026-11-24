from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .ec2_capacity_reservation import EC2CapacityReservation


class EC2MoveCapacityReservationInstancesResponse(BaseModel):
    SourceCapacityReservation: EC2CapacityReservation | None = None
    DestinationCapacityReservation: EC2CapacityReservation | None = None
    InstanceCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
