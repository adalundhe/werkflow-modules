from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTAddThingsToThingGroupParams(BaseModel):
    thingGroupNames: list[StrictStr] | None = None
    overrideDynamicGroups: StrictBool | None = None
