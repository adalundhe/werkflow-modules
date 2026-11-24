from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_group_profile_summary import DataZoneGroupProfileSummary


class DataZoneSearchGroupProfilesResponse(BaseModel):
    items: list[DataZoneGroupProfileSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
