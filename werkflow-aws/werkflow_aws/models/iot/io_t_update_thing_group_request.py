from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_thing_group_properties import IoTThingGroupProperties


class IoTUpdateThingGroupRequest(BaseModel):
    thingGroupName: StrictStr
    thingGroupProperties: IoTThingGroupProperties
    expectedVersion: StrictInt | None = None
