from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_thing_type_metadata import IoTThingTypeMetadata
from .io_t_thing_type_properties import IoTThingTypeProperties


class IoTDescribeThingTypeResponse(BaseModel):
    thingTypeName: StrictStr | None = None
    thingTypeId: StrictStr | None = None
    thingTypeArn: StrictStr | None = None
    thingTypeProperties: IoTThingTypeProperties | None = None
    thingTypeMetadata: IoTThingTypeMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
