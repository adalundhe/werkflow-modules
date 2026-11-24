from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_mqtt5_configuration import IoTMqtt5Configuration


class IoTThingTypeProperties(BaseModel):
    thingTypeDescription: StrictStr | None = None
    searchableAttributes: list[StrictStr] | None = None
    mqtt5Configuration: IoTMqtt5Configuration | None = None
