from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LocationCreateGeofenceCollectionRequest(BaseModel):
    CollectionName: StrictStr
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    PricingPlanDataSource: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    KmsKeyId: StrictStr | None = None
