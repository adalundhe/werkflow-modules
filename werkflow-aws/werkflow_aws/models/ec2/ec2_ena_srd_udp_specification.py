from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2EnaSrdUdpSpecification(BaseModel):
    EnaSrdUdpEnabled: StrictBool | None = None
