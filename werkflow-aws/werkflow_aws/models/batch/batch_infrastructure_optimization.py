from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BatchInfrastructureOptimization(BaseModel):
    scaleInAfter: StrictInt | None = None
