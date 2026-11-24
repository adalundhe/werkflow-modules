from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_service_resource_id import BatchServiceResourceId


class BatchServiceJobAttemptDetail(BaseModel):
    serviceResourceId: BatchServiceResourceId | None = None
    startedAt: StrictInt | None = None
    stoppedAt: StrictInt | None = None
    statusReason: StrictStr | None = None
