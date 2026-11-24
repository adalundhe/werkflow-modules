from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_attempt_container_detail import BatchAttemptContainerDetail
from .batch_attempt_ecs_task_details import BatchAttemptEcsTaskDetails


class BatchAttemptDetail(BaseModel):
    container: BatchAttemptContainerDetail | None = None
    startedAt: StrictInt | None = None
    stoppedAt: StrictInt | None = None
    statusReason: StrictStr | None = None
    taskProperties: list[BatchAttemptEcsTaskDetails] | None = None
