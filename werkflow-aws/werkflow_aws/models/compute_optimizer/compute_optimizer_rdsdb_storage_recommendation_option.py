from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_db_storage_configuration import ComputeOptimizerDBStorageConfiguration
from .compute_optimizer_rds_storage_savings_opportunity_after_discounts import ComputeOptimizerRDSStorageSavingsOpportunityAfterDiscounts
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity


class ComputeOptimizerRDSDBStorageRecommendationOption(BaseModel):
    storageConfiguration: ComputeOptimizerDBStorageConfiguration | None = None
    rank: StrictInt | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    savingsOpportunityAfterDiscounts: ComputeOptimizerRDSStorageSavingsOpportunityAfterDiscounts | None = None
    estimatedMonthlyVolumeIOPsCostVariation: StrictStr | None = None
