from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CostExplorerESInstanceDetails(BaseModel):
    InstanceClass: StrictStr | None = None
    InstanceSize: StrictStr | None = None
    Region: StrictStr | None = None
    CurrentGeneration: StrictBool | None = None
    SizeFlexEligible: StrictBool | None = None
