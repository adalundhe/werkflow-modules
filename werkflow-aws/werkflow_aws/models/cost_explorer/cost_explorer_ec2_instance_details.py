from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CostExplorerEC2InstanceDetails(BaseModel):
    Family: StrictStr | None = None
    InstanceType: StrictStr | None = None
    Region: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Platform: StrictStr | None = None
    Tenancy: StrictStr | None = None
    CurrentGeneration: StrictBool | None = None
    SizeFlexEligible: StrictBool | None = None
