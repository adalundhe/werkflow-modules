from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComputeOptimizerLambdaEstimatedMonthlySavings(BaseModel):
    currency: StrictStr | None = None
    value: StrictFloat | StrictInt | None = None
