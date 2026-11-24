from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTRemoveThingFromThingGroupRequest(BaseModel):
    thingGroupName: StrictStr | None = None
    thingGroupArn: StrictStr | None = None
    thingName: StrictStr | None = None
    thingArn: StrictStr | None = None
