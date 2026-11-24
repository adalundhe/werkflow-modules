from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2PortRange(BaseModel):
    From: StrictInt | None = None
    To: StrictInt | None = None
