from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_path_statistics import WAFv2PathStatistics


class WAFv2GetTopPathStatisticsByTrafficResponse(BaseModel):
    PathStatistics: list[WAFv2PathStatistics] | None = None
    TotalRequestCount: StrictInt | None = None
    NextMarker: StrictStr | None = None
    TopCategories: list[WAFv2PathStatistics] | None = None
    ResponseMetadata: dict[str, Any] | None = None
