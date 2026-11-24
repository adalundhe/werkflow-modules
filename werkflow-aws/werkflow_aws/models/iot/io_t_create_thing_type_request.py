from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag
from .io_t_thing_type_properties import IoTThingTypeProperties


class IoTCreateThingTypeRequest(BaseModel):
    thingTypeName: StrictStr
    thingTypeProperties: IoTThingTypeProperties | None = None
    tags: list[IoTTag] | None = None
