from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_project_profile_summary import DataZoneProjectProfileSummary


class DataZoneListProjectProfilesResponse(BaseModel):
    items: list[DataZoneProjectProfileSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
