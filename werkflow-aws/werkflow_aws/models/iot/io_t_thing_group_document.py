from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTThingGroupDocument(BaseModel):
    thingGroupName: StrictStr | None = None
    thingGroupId: StrictStr | None = None
    thingGroupDescription: StrictStr | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    parentGroupNames: list[StrictStr] | None = None
