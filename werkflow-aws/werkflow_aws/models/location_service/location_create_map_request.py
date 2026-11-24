from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .location_map_configuration import LocationMapConfiguration


class LocationCreateMapRequest(BaseModel):
    MapName: StrictStr
    Configuration: LocationMapConfiguration
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
