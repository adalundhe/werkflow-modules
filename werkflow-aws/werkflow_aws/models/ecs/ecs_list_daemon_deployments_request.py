from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_created_at import ECSCreatedAt


class ECSListDaemonDeploymentsRequest(BaseModel):
    daemonArn: StrictStr
    status: list[Literal['PENDING', 'SUCCESSFUL', 'STOPPED', 'STOP_REQUESTED', 'IN_PROGRESS', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCESSFUL', 'ROLLBACK_FAILED']] | None = None
    createdAt: ECSCreatedAt | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
