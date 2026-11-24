from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_group_identifier import EC2GroupIdentifier
from .ec2_instance import EC2Instance


class EC2Reservation(BaseModel):
    ReservationId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    RequesterId: StrictStr | None = None
    Groups: list[EC2GroupIdentifier] | None = None
    Instances: list[EC2Instance] | None = None
