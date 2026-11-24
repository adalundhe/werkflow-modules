from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag
from .io_t_thing_group_properties import IoTThingGroupProperties


class IoTCreateThingGroupRequest(BaseModel):
    thingGroupName: StrictStr
    parentGroupName: StrictStr | None = None
    thingGroupProperties: IoTThingGroupProperties | None = None
    tags: list[IoTTag] | None = None
