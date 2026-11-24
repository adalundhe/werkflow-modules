from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListServicesRequest(BaseModel):
    cluster: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    launchType: Literal['EC2', 'FARGATE', 'EXTERNAL', 'MANAGED_INSTANCES'] | None = None
    schedulingStrategy: Literal['REPLICA', 'DAEMON'] | None = None
    resourceManagementType: Literal['CUSTOMER', 'ECS'] | None = None
