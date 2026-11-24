from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .location_map_configuration_update import LocationMapConfigurationUpdate


class LocationUpdateMapRequest(BaseModel):
    MapName: StrictStr
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    Description: StrictStr | None = None
    ConfigurationUpdate: LocationMapConfigurationUpdate | None = None
