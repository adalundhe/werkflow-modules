from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_environment_blueprint_configuration_item import DataZoneEnvironmentBlueprintConfigurationItem


class DataZoneListEnvironmentBlueprintConfigurationsResponse(BaseModel):
    items: list[DataZoneEnvironmentBlueprintConfigurationItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
