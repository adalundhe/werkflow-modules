from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_time_series_data_point_form_input import DataZoneTimeSeriesDataPointFormInput


class DataZonePostTimeSeriesDataPointsRequest(BaseModel):
    domainIdentifier: StrictStr
    entityIdentifier: StrictStr
    entityType: Literal['ASSET', 'LISTING']
    forms: list[DataZoneTimeSeriesDataPointFormInput]
    clientToken: StrictStr | None = None
