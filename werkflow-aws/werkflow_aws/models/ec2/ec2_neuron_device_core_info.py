from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2NeuronDeviceCoreInfo(BaseModel):
    Count: StrictInt | None = None
    Version: StrictInt | None = None
