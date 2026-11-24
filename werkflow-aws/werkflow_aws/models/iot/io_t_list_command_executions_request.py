from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_time_filter import IoTTimeFilter


class IoTListCommandExecutionsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    namespace: Literal['AWS-IoT', 'AWS-IoT-FleetWise'] | None = None
    status: Literal['CREATED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'REJECTED', 'TIMED_OUT'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    startedTimeFilter: IoTTimeFilter | None = None
    completedTimeFilter: IoTTimeFilter | None = None
    targetArn: StrictStr | None = None
    commandArn: StrictStr | None = None
