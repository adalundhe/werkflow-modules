from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_data_source_summary import DataZoneDataSourceSummary


class DataZoneListDataSourcesResponse(BaseModel):
    items: list[DataZoneDataSourceSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
