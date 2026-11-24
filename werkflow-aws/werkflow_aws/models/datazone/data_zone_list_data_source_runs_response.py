from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_data_source_run_summary import DataZoneDataSourceRunSummary


class DataZoneListDataSourceRunsResponse(BaseModel):
    items: list[DataZoneDataSourceRunSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
