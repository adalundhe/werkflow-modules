from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity


class ComputeOptimizerLicenseRecommendationOption(BaseModel):
    rank: StrictInt | None = None
    operatingSystem: StrictStr | None = None
    licenseEdition: StrictStr | None = None
    licenseModel: StrictStr | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
