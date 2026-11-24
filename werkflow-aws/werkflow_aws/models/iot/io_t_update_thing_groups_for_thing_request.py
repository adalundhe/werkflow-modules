from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTUpdateThingGroupsForThingRequest(BaseModel):
    thingName: StrictStr | None = None
    thingGroupsToAdd: list[StrictStr] | None = None
    thingGroupsToRemove: list[StrictStr] | None = None
    overrideDynamicGroups: StrictBool | None = None
