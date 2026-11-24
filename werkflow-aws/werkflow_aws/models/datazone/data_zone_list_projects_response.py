from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_project_summary import DataZoneProjectSummary


class DataZoneListProjectsResponse(BaseModel):
    items: list[DataZoneProjectSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
