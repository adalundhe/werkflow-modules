from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerRecommendationDetailHourlyMetrics(BaseModel):
    StartTime: StrictStr | None = None
    EstimatedOnDemandCost: StrictStr | None = None
    CurrentCoverage: StrictStr | None = None
    EstimatedCoverage: StrictStr | None = None
    EstimatedNewCommitmentUtilization: StrictStr | None = None
