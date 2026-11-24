from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerEBSSavingsEstimationMode(BaseModel):
    source: StrictStr | None = None
