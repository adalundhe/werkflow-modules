from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SupportTrustedAdvisorCostOptimizingSummary(BaseModel):
    estimatedMonthlySavings: StrictFloat | StrictInt | None = None
    estimatedPercentMonthlySavings: StrictFloat | StrictInt | None = None
