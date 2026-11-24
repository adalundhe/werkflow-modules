from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_map_configuration import LocationMapConfiguration


class LocationDescribeMapResponse(BaseModel):
    MapName: StrictStr | None = None
    MapArn: StrictStr | None = None
    PricingPlan: StrictStr | None = None
    DataSource: StrictStr | None = None
    Configuration: LocationMapConfiguration | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
