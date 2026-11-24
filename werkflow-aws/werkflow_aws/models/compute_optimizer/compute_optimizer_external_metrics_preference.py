from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerExternalMetricsPreference(BaseModel):
    source: StrictStr | None = None
