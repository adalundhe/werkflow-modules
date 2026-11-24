from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerReservationAggregates(BaseModel):
    UtilizationPercentage: StrictStr | None = None
    UtilizationPercentageInUnits: StrictStr | None = None
    PurchasedHours: StrictStr | None = None
    PurchasedUnits: StrictStr | None = None
    TotalActualHours: StrictStr | None = None
    TotalActualUnits: StrictStr | None = None
    UnusedHours: StrictStr | None = None
    UnusedUnits: StrictStr | None = None
    OnDemandCostOfRIHoursUsed: StrictStr | None = None
    NetRISavings: StrictStr | None = None
    TotalPotentialRISavings: StrictStr | None = None
    AmortizedUpfrontFee: StrictStr | None = None
    AmortizedRecurringFee: StrictStr | None = None
    TotalAmortizedFee: StrictStr | None = None
    RICostForUnusedHours: StrictStr | None = None
    RealizedSavings: StrictStr | None = None
    UnrealizedSavings: StrictStr | None = None
