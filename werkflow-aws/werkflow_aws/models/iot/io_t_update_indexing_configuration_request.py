from __future__ import annotations
from pydantic import BaseModel
from .io_t_thing_group_indexing_configuration import IoTThingGroupIndexingConfiguration
from .io_t_thing_indexing_configuration import IoTThingIndexingConfiguration


class IoTUpdateIndexingConfigurationRequest(BaseModel):
    thingIndexingConfiguration: IoTThingIndexingConfiguration | None = None
    thingGroupIndexingConfiguration: IoTThingGroupIndexingConfiguration | None = None
