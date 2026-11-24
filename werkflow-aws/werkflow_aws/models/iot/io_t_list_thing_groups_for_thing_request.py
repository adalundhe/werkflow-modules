from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListThingGroupsForThingRequest(BaseModel):
    thingName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
