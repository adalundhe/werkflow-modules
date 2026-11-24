from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_search_types_result_item import DataZoneSearchTypesResultItem


class DataZoneSearchTypesResponse(BaseModel):
    items: list[DataZoneSearchTypesResultItem] | None = None
    nextToken: StrictStr | None = None
    totalMatchCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
