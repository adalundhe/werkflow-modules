from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_environment_summary import DataZoneEnvironmentSummary


class DataZoneListEnvironmentsResponse(BaseModel):
    items: list[DataZoneEnvironmentSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
