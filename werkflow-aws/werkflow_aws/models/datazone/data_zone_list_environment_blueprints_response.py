from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_environment_blueprint_summary import DataZoneEnvironmentBlueprintSummary


class DataZoneListEnvironmentBlueprintsResponse(BaseModel):
    items: list[DataZoneEnvironmentBlueprintSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
