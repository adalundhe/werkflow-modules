from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_search_inventory_result_item import DataZoneSearchInventoryResultItem


class DataZoneSearchResponse(BaseModel):
    items: list[DataZoneSearchInventoryResultItem] | None = None
    nextToken: StrictStr | None = None
    totalMatchCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
