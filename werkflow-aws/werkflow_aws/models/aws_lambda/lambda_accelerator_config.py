from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaAcceleratorConfig(BaseModel):
    AcceleratorMemorySize: StrictInt
