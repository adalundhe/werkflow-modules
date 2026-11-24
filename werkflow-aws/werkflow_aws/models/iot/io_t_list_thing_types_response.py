from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_thing_type_definition import IoTThingTypeDefinition


class IoTListThingTypesResponse(BaseModel):
    thingTypes: list[IoTThingTypeDefinition] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
