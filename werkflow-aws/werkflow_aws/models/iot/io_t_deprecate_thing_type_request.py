from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTDeprecateThingTypeRequest(BaseModel):
    thingTypeName: StrictStr
    undoDeprecate: StrictBool | None = None
