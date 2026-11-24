from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LocationUpdateRouteCalculatorRequest(BaseModel):
    CalculatorName: StrictStr
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    Description: StrictStr | None = None
