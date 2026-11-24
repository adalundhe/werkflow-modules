from __future__ import annotations
from pydantic import BaseModel
from .ec2_modification_reservation_update import EC2ModificationReservationUpdate


class EC2ModificationTerms(BaseModel):
    ReservationUpdate: EC2ModificationReservationUpdate | None = None
