from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class LocationUpdateTrackerRequest(BaseModel):
    TrackerName: StrictStr
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    PricingPlanDataSource: StrictStr | None = None
    Description: StrictStr | None = None
    PositionFiltering: Literal['TimeBased', 'DistanceBased', 'AccuracyBased'] | None = None
    EventBridgeEnabled: StrictBool | None = None
    KmsKeyEnableGeospatialQueries: StrictBool | None = None
