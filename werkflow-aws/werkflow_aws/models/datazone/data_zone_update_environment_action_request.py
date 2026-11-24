from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_action_parameters import DataZoneActionParameters


class DataZoneUpdateEnvironmentActionRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    identifier: StrictStr
    parameters: DataZoneActionParameters | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
