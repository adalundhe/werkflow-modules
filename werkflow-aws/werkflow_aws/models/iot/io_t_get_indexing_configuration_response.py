from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_thing_group_indexing_configuration import IoTThingGroupIndexingConfiguration
from .io_t_thing_indexing_configuration import IoTThingIndexingConfiguration


class IoTGetIndexingConfigurationResponse(BaseModel):
    thingIndexingConfiguration: IoTThingIndexingConfiguration | None = None
    thingGroupIndexingConfiguration: IoTThingGroupIndexingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
