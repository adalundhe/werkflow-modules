from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_data_source_run_activity import DataZoneDataSourceRunActivity


class DataZoneListDataSourceRunActivitiesResponse(BaseModel):
    items: list[DataZoneDataSourceRunActivity] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
