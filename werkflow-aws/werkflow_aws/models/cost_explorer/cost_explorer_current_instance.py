from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_resource_details import CostExplorerResourceDetails
from .cost_explorer_resource_utilization import CostExplorerResourceUtilization
from .cost_explorer_tag_values import CostExplorerTagValues


class CostExplorerCurrentInstance(BaseModel):
    ResourceId: StrictStr | None = None
    InstanceName: StrictStr | None = None
    Tags: list[CostExplorerTagValues] | None = None
    ResourceDetails: CostExplorerResourceDetails | None = None
    ResourceUtilization: CostExplorerResourceUtilization | None = None
    ReservationCoveredHoursInLookbackPeriod: StrictStr | None = None
    SavingsPlansCoveredHoursInLookbackPeriod: StrictStr | None = None
    OnDemandHoursInLookbackPeriod: StrictStr | None = None
    TotalRunningHoursInLookbackPeriod: StrictStr | None = None
    MonthlyCost: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
