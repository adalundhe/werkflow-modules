from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListAuditMitigationActionsExecutionsRequest(BaseModel):
    taskId: StrictStr
    findingId: StrictStr
    actionStatus: Literal['IN_PROGRESS', 'COMPLETED', 'FAILED', 'CANCELED', 'SKIPPED', 'PENDING'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
