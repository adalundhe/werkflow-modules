from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerLambdaSavingsEstimationMode(BaseModel):
    source: StrictStr | None = None
