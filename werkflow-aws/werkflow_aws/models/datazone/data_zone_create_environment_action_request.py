from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_action_parameters import DataZoneActionParameters


class DataZoneCreateEnvironmentActionRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    name: StrictStr
    parameters: DataZoneActionParameters
    description: StrictStr | None = None
