from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_recommendation_detail_hourly_metrics import CostExplorerRecommendationDetailHourlyMetrics


class CostExplorerRecommendationDetailData(BaseModel):
    AccountScope: StrictStr | None = None
    LookbackPeriodInDays: StrictStr | None = None
    SavingsPlansType: StrictStr | None = None
    TermInYears: StrictStr | None = None
    PaymentOption: StrictStr | None = None
    AccountId: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    Region: StrictStr | None = None
    OfferingId: StrictStr | None = None
    GenerationTimestamp: StrictStr | None = None
    LatestUsageTimestamp: StrictStr | None = None
    CurrentAverageHourlyOnDemandSpend: StrictStr | None = None
    CurrentMaximumHourlyOnDemandSpend: StrictStr | None = None
    CurrentMinimumHourlyOnDemandSpend: StrictStr | None = None
    EstimatedAverageUtilization: StrictStr | None = None
    EstimatedMonthlySavingsAmount: StrictStr | None = None
    EstimatedOnDemandCost: StrictStr | None = None
    EstimatedOnDemandCostWithCurrentCommitment: StrictStr | None = None
    EstimatedROI: StrictStr | None = None
    EstimatedSPCost: StrictStr | None = None
    EstimatedSavingsAmount: StrictStr | None = None
    EstimatedSavingsPercentage: StrictStr | None = None
    ExistingHourlyCommitment: StrictStr | None = None
    HourlyCommitmentToPurchase: StrictStr | None = None
    UpfrontCost: StrictStr | None = None
    CurrentAverageCoverage: StrictStr | None = None
    EstimatedAverageCoverage: StrictStr | None = None
    MetricsOverLookbackPeriod: list[CostExplorerRecommendationDetailHourlyMetrics] | None = None
