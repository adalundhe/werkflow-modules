from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LocationCreateRouteCalculatorRequest(BaseModel):
    CalculatorName: StrictStr
    DataSource: StrictStr
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
