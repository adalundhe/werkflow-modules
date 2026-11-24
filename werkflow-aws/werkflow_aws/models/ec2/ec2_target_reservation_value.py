from __future__ import annotations
from pydantic import BaseModel
from .ec2_reservation_value import EC2ReservationValue
from .ec2_target_configuration import EC2TargetConfiguration


class EC2TargetReservationValue(BaseModel):
    ReservationValue: EC2ReservationValue | None = None
    TargetConfiguration: EC2TargetConfiguration | None = None
