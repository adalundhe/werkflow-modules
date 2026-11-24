from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_instance_details import CostExplorerInstanceDetails
from .cost_explorer_reserved_capacity_details import CostExplorerReservedCapacityDetails


class CostExplorerReservationPurchaseRecommendationDetail(BaseModel):
    AccountId: StrictStr | None = None
    InstanceDetails: CostExplorerInstanceDetails | None = None
    RecommendedNumberOfInstancesToPurchase: StrictStr | None = None
    RecommendedNormalizedUnitsToPurchase: StrictStr | None = None
    MinimumNumberOfInstancesUsedPerHour: StrictStr | None = None
    MinimumNormalizedUnitsUsedPerHour: StrictStr | None = None
    MaximumNumberOfInstancesUsedPerHour: StrictStr | None = None
    MaximumNormalizedUnitsUsedPerHour: StrictStr | None = None
    AverageNumberOfInstancesUsedPerHour: StrictStr | None = None
    AverageNormalizedUnitsUsedPerHour: StrictStr | None = None
    AverageUtilization: StrictStr | None = None
    EstimatedBreakEvenInMonths: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    EstimatedMonthlySavingsAmount: StrictStr | None = None
    EstimatedMonthlySavingsPercentage: StrictStr | None = None
    EstimatedMonthlyOnDemandCost: StrictStr | None = None
    EstimatedReservationCostForLookbackPeriod: StrictStr | None = None
    UpfrontCost: StrictStr | None = None
    RecurringStandardMonthlyCost: StrictStr | None = None
    ReservedCapacityDetails: CostExplorerReservedCapacityDetails | None = None
    RecommendedNumberOfCapacityUnitsToPurchase: StrictStr | None = None
    MinimumNumberOfCapacityUnitsUsedPerHour: StrictStr | None = None
    MaximumNumberOfCapacityUnitsUsedPerHour: StrictStr | None = None
    AverageNumberOfCapacityUnitsUsedPerHour: StrictStr | None = None
