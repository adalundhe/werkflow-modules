from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2EfaInfo(BaseModel):
    MaximumEfaInterfaces: StrictInt | None = None
