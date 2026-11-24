from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerCustomizableMetricParameters(BaseModel):
    threshold: StrictStr | None = None
    headroom: StrictStr | None = None
