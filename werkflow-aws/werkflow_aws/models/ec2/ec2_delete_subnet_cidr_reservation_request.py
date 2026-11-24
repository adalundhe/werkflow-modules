from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteSubnetCidrReservationRequest(BaseModel):
    SubnetCidrReservationId: StrictStr
    DryRun: StrictBool | None = None
