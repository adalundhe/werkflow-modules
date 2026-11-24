from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2EnaSrdUdpSpecificationRequest(BaseModel):
    EnaSrdUdpEnabled: StrictBool | None = None
