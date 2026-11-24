from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_thing_group_properties import IoTThingGroupProperties


class IoTUpdateDynamicThingGroupRequest(BaseModel):
    thingGroupName: StrictStr
    thingGroupProperties: IoTThingGroupProperties
    expectedVersion: StrictInt | None = None
    indexName: StrictStr | None = None
    queryString: StrictStr | None = None
    queryVersion: StrictStr | None = None
