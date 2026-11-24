from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ELBv2MinimumLoadBalancerCapacity(BaseModel):
    CapacityUnits: StrictInt | None = None
