from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerInstanceSavingsEstimationMode(BaseModel):
    source: StrictStr | None = None
