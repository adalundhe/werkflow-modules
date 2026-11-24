from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation_target_response import EC2CapacityReservationTargetResponse


class EC2LaunchTemplateCapacityReservationSpecificationResponse(BaseModel):
    CapacityReservationPreference: StrictStr | None = None
    CapacityReservationTarget: EC2CapacityReservationTargetResponse | None = None
