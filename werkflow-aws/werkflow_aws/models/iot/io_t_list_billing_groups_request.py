from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListBillingGroupsRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    namePrefixFilter: StrictStr | None = None
