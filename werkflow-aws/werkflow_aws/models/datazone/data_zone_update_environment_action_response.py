from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_action_parameters import DataZoneActionParameters


class DataZoneUpdateEnvironmentActionResponse(BaseModel):
    domainId: StrictStr | None = None
    environmentId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    parameters: DataZoneActionParameters | None = None
    description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
