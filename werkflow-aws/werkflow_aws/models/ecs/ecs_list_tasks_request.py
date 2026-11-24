from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListTasksRequest(BaseModel):
    cluster: StrictStr | None = None
    containerInstance: StrictStr | None = None
    family: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    startedBy: StrictStr | None = None
    serviceName: StrictStr | None = None
    desiredStatus: Literal['RUNNING', 'PENDING', 'STOPPED'] | None = None
    launchType: Literal['EC2', 'FARGATE', 'EXTERNAL', 'MANAGED_INSTANCES'] | None = None
    daemonName: StrictStr | None = None
