from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_action_parameters import DataZoneActionParameters


class DataZoneEnvironmentActionSummary(BaseModel):
    domainId: StrictStr | None = None
    environmentId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    parameters: DataZoneActionParameters | None = None
    description: StrictStr | None = None
