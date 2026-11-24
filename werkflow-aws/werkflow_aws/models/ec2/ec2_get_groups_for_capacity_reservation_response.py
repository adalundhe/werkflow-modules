from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation_group import EC2CapacityReservationGroup


class EC2GetGroupsForCapacityReservationResponse(BaseModel):
    NextToken: StrictStr | None = None
    CapacityReservationGroups: list[EC2CapacityReservationGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
