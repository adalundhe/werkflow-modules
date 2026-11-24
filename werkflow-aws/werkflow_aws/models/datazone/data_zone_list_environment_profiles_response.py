from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_environment_profile_summary import DataZoneEnvironmentProfileSummary


class DataZoneListEnvironmentProfilesResponse(BaseModel):
    items: list[DataZoneEnvironmentProfileSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
