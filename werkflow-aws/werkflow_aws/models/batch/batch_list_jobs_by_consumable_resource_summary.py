from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_consumable_resource_properties import BatchConsumableResourceProperties


class BatchListJobsByConsumableResourceSummary(BaseModel):
    jobArn: StrictStr | None = None
    jobQueueArn: StrictStr | None = None
    jobName: StrictStr | None = None
    jobDefinitionArn: StrictStr | None = None
    shareIdentifier: StrictStr | None = None
    jobStatus: StrictStr | None = None
    quantity: StrictInt | None = None
    statusReason: StrictStr | None = None
    startedAt: StrictInt | None = None
    createdAt: StrictInt | None = None
    consumableResourceProperties: BatchConsumableResourceProperties | None = None
