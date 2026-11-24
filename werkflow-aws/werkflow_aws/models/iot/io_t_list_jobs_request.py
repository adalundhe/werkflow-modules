from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListJobsRequest(BaseModel):
    status: Literal['IN_PROGRESS', 'CANCELED', 'COMPLETED', 'DELETION_IN_PROGRESS', 'SCHEDULED'] | None = None
    targetSelection: Literal['CONTINUOUS', 'SNAPSHOT'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    thingGroupName: StrictStr | None = None
    thingGroupId: StrictStr | None = None
    namespaceId: StrictStr | None = None
