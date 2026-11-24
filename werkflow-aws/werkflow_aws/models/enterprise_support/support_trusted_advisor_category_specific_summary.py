from __future__ import annotations
from pydantic import BaseModel
from .support_trusted_advisor_cost_optimizing_summary import SupportTrustedAdvisorCostOptimizingSummary


class SupportTrustedAdvisorCategorySpecificSummary(BaseModel):
    costOptimizing: SupportTrustedAdvisorCostOptimizingSummary | None = None
