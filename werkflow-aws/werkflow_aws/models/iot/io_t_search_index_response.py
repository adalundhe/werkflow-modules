from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_thing_document import IoTThingDocument
from .io_t_thing_group_document import IoTThingGroupDocument


class IoTSearchIndexResponse(BaseModel):
    nextToken: StrictStr | None = None
    things: list[IoTThingDocument] | None = None
    thingGroups: list[IoTThingGroupDocument] | None = None
    ResponseMetadata: dict[str, Any] | None = None
