from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListCommandsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    namespace: Literal['AWS-IoT', 'AWS-IoT-FleetWise'] | None = None
    commandParameterName: StrictStr | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
