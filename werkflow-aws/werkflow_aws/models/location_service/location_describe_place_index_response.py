from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_data_source_configuration import LocationDataSourceConfiguration


class LocationDescribePlaceIndexResponse(BaseModel):
    IndexName: StrictStr | None = None
    IndexArn: StrictStr | None = None
    PricingPlan: StrictStr | None = None
    Description: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    DataSource: StrictStr | None = None
    DataSourceConfiguration: LocationDataSourceConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
