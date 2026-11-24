from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2SubnetCidrReservation(BaseModel):
    SubnetCidrReservationId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    Cidr: StrictStr | None = None
    ReservationType: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
