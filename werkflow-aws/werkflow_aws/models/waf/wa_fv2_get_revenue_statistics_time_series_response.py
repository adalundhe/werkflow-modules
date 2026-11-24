from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_data_point_entry import WAFv2DataPointEntry


class WAFv2GetRevenueStatisticsTimeSeriesResponse(BaseModel):
    DataPoints: list[WAFv2DataPointEntry] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
