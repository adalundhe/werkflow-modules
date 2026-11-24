from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerECSSavingsEstimationMode(BaseModel):
    source: StrictStr | None = None
