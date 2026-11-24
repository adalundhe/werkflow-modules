from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_revenue_path_statistics import WAFv2RevenuePathStatistics
from .wa_fv2_source_statistics import WAFv2SourceStatistics


class WAFv2GetRevenueStatisticsResponse(BaseModel):
    SourceStatistics: list[WAFv2SourceStatistics] | None = None
    RevenuePathStatistics: list[WAFv2RevenuePathStatistics] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
