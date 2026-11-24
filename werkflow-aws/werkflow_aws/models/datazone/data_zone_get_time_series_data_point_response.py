from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_time_series_data_point_form_output import DataZoneTimeSeriesDataPointFormOutput


class DataZoneGetTimeSeriesDataPointResponse(BaseModel):
    domainId: StrictStr | None = None
    entityId: StrictStr | None = None
    entityType: StrictStr | None = None
    formName: StrictStr | None = None
    form: DataZoneTimeSeriesDataPointFormOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
