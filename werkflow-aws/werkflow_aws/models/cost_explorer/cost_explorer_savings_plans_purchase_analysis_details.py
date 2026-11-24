from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_recommendation_detail_hourly_metrics import CostExplorerRecommendationDetailHourlyMetrics


class CostExplorerSavingsPlansPurchaseAnalysisDetails(BaseModel):
    CurrencyCode: StrictStr | None = None
    LookbackPeriodInHours: StrictStr | None = None
    CurrentAverageCoverage: StrictStr | None = None
    CurrentAverageHourlyOnDemandSpend: StrictStr | None = None
    CurrentMaximumHourlyOnDemandSpend: StrictStr | None = None
    CurrentMinimumHourlyOnDemandSpend: StrictStr | None = None
    CurrentOnDemandSpend: StrictStr | None = None
    ExistingHourlyCommitment: StrictStr | None = None
    HourlyCommitmentToPurchase: StrictStr | None = None
    EstimatedAverageCoverage: StrictStr | None = None
    EstimatedAverageUtilization: StrictStr | None = None
    EstimatedMonthlySavingsAmount: StrictStr | None = None
    EstimatedOnDemandCost: StrictStr | None = None
    EstimatedOnDemandCostWithCurrentCommitment: StrictStr | None = None
    EstimatedROI: StrictStr | None = None
    EstimatedSavingsAmount: StrictStr | None = None
    EstimatedSavingsPercentage: StrictStr | None = None
    EstimatedCommitmentCost: StrictStr | None = None
    LatestUsageTimestamp: StrictStr | None = None
    UpfrontCost: StrictStr | None = None
    AdditionalMetadata: StrictStr | None = None
    MetricsOverLookbackPeriod: list[CostExplorerRecommendationDetailHourlyMetrics] | None = None
