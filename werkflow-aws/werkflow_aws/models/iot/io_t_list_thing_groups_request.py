from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListThingGroupsRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    parentGroup: StrictStr | None = None
    namePrefixFilter: StrictStr | None = None
    recursive: StrictBool | None = None
