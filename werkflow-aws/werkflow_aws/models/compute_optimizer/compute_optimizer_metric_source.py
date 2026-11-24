from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerMetricSource(BaseModel):
    provider: StrictStr | None = None
    providerArn: StrictStr | None = None
