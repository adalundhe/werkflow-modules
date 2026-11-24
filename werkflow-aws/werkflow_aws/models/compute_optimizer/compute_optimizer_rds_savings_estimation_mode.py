from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerRDSSavingsEstimationMode(BaseModel):
    source: StrictStr | None = None
