from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListThingTypesRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    thingTypeName: StrictStr | None = None
