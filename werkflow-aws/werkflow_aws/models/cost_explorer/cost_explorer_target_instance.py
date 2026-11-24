from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cost_explorer_resource_details import CostExplorerResourceDetails
from .cost_explorer_resource_utilization import CostExplorerResourceUtilization


class CostExplorerTargetInstance(BaseModel):
    EstimatedMonthlyCost: StrictStr | None = None
    EstimatedMonthlySavings: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    DefaultTargetInstance: StrictBool | None = None
    ResourceDetails: CostExplorerResourceDetails | None = None
    ExpectedResourceUtilization: CostExplorerResourceUtilization | None = None
    PlatformDifferences: list[StrictStr] | None = None
