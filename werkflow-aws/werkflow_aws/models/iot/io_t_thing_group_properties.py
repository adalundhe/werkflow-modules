from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_attribute_payload import IoTAttributePayload


class IoTThingGroupProperties(BaseModel):
    thingGroupDescription: StrictStr | None = None
    attributePayload: IoTAttributePayload | None = None
