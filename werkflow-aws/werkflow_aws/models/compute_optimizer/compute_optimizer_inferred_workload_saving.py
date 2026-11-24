from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .compute_optimizer_estimated_monthly_savings import ComputeOptimizerEstimatedMonthlySavings


class ComputeOptimizerInferredWorkloadSaving(BaseModel):
    inferredWorkloadTypes: list[StrictStr] | None = None
    estimatedMonthlySavings: ComputeOptimizerEstimatedMonthlySavings | None = None
