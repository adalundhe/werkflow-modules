from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2MovingAddressStatus(BaseModel):
    MoveStatus: StrictStr | None = None
    PublicIp: StrictStr | None = None
