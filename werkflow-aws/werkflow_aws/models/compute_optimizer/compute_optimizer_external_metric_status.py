from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerExternalMetricStatus(BaseModel):
    statusCode: StrictStr | None = None
    statusReason: StrictStr | None = None
