from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_thing_type_properties import IoTThingTypeProperties


class IoTUpdateThingTypeRequest(BaseModel):
    thingTypeName: StrictStr
    thingTypeProperties: IoTThingTypeProperties | None = None
