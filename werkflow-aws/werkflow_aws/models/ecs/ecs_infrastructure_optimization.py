from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ECSInfrastructureOptimization(BaseModel):
    scaleInAfter: StrictInt | None = None
