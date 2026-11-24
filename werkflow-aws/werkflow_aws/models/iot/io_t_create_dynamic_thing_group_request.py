from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag
from .io_t_thing_group_properties import IoTThingGroupProperties


class IoTCreateDynamicThingGroupRequest(BaseModel):
    thingGroupName: StrictStr
    queryString: StrictStr
    thingGroupProperties: IoTThingGroupProperties | None = None
    indexName: StrictStr | None = None
    queryVersion: StrictStr | None = None
    tags: list[IoTTag] | None = None
