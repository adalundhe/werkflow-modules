from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTAddThingToThingGroupRequest(BaseModel):
    thingGroupName: StrictStr | None = None
    thingGroupArn: StrictStr | None = None
    thingName: StrictStr | None = None
    thingArn: StrictStr | None = None
    overrideDynamicGroups: StrictBool | None = None
