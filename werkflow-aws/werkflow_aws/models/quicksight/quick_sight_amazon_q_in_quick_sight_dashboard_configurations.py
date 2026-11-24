from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_executive_summary_configurations import QuickSightExecutiveSummaryConfigurations


class QuickSightAmazonQInQuickSightDashboardConfigurations(BaseModel):
    ExecutiveSummary: QuickSightExecutiveSummaryConfigurations | None = None
