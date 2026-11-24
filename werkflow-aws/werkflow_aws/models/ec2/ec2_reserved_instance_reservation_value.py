from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_reservation_value import EC2ReservationValue


class EC2ReservedInstanceReservationValue(BaseModel):
    ReservationValue: EC2ReservationValue | None = None
    ReservedInstanceId: StrictStr | None = None
