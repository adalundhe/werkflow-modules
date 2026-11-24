from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_environment_action_summary import DataZoneEnvironmentActionSummary


class DataZoneListEnvironmentActionsResponse(BaseModel):
    items: list[DataZoneEnvironmentActionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
