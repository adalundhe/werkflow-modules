from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_attribute_payload import IoTAttributePayload


class IoTCreateThingRequest(BaseModel):
    thingName: StrictStr
    thingTypeName: StrictStr | None = None
    attributePayload: IoTAttributePayload | None = None
    billingGroupName: StrictStr | None = None
