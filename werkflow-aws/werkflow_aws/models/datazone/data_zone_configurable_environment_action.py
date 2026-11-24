from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_configurable_action_parameter import DataZoneConfigurableActionParameter


class DataZoneConfigurableEnvironmentAction(BaseModel):
    type: StrictStr | None = None
    auth: StrictStr | None = None
    parameters: list[DataZoneConfigurableActionParameter] | None = None
