from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_created_at import ECSCreatedAt


class ECSListServiceDeploymentsRequest(BaseModel):
    service: StrictStr
    cluster: StrictStr | None = None
    status: list[Literal['PENDING', 'SUCCESSFUL', 'STOPPED', 'STOP_REQUESTED', 'IN_PROGRESS', 'ROLLBACK_REQUESTED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCESSFUL', 'ROLLBACK_FAILED']] | None = None
    createdAt: ECSCreatedAt | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
