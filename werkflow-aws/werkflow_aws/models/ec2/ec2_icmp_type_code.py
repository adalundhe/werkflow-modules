from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2IcmpTypeCode(BaseModel):
    Code: StrictInt | None = None
    Type: StrictInt | None = None
