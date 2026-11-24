from __future__ import annotations
from pydantic import BaseModel
from .batch_service_resource_id import BatchServiceResourceId


class BatchLatestServiceJobAttempt(BaseModel):
    serviceResourceId: BatchServiceResourceId | None = None
