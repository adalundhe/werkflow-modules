from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListThingsInThingGroupRequest(BaseModel):
    thingGroupName: StrictStr
    recursive: StrictBool | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
