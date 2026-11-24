from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LocationUpdateGeofenceCollectionRequest(BaseModel):
    CollectionName: StrictStr
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    PricingPlanDataSource: StrictStr | None = None
    Description: StrictStr | None = None
