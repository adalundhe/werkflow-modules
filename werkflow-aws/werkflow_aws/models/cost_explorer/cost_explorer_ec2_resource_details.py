from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerEC2ResourceDetails(BaseModel):
    HourlyOnDemandRate: StrictStr | None = None
    InstanceType: StrictStr | None = None
    Platform: StrictStr | None = None
    Region: StrictStr | None = None
    Sku: StrictStr | None = None
    Memory: StrictStr | None = None
    NetworkPerformance: StrictStr | None = None
    Storage: StrictStr | None = None
    Vcpu: StrictStr | None = None
