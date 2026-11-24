from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2VolumeDetail(BaseModel):
    Size: StrictInt
