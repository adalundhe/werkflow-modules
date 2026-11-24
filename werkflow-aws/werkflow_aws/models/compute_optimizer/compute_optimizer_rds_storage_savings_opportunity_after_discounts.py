from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_rds_storage_estimated_monthly_savings import ComputeOptimizerRDSStorageEstimatedMonthlySavings


class ComputeOptimizerRDSStorageSavingsOpportunityAfterDiscounts(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerRDSStorageEstimatedMonthlySavings | None = None
