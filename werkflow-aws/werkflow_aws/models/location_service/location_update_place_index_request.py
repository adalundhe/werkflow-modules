from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .location_data_source_configuration import LocationDataSourceConfiguration


class LocationUpdatePlaceIndexRequest(BaseModel):
    IndexName: StrictStr
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    Description: StrictStr | None = None
    DataSourceConfiguration: LocationDataSourceConfiguration | None = None
