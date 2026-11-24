from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .io_t_attribute_payload import IoTAttributePayload


class IoTUpdateThingRequest(BaseModel):
    thingName: StrictStr
    thingTypeName: StrictStr | None = None
    attributePayload: IoTAttributePayload | None = None
    expectedVersion: StrictInt | None = None
    removeThingType: StrictBool | None = None
