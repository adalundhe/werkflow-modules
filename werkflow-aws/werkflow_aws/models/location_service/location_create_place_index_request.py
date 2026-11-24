from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .location_data_source_configuration import LocationDataSourceConfiguration


class LocationCreatePlaceIndexRequest(BaseModel):
    IndexName: StrictStr
    DataSource: StrictStr
    PricingPlan: Literal['RequestBasedUsage', 'MobileAssetTracking', 'MobileAssetManagement'] | None = None
    Description: StrictStr | None = None
    DataSourceConfiguration: LocationDataSourceConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
