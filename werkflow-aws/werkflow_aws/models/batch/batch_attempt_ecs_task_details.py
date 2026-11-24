from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_attempt_task_container_details import BatchAttemptTaskContainerDetails


class BatchAttemptEcsTaskDetails(BaseModel):
    containerInstanceArn: StrictStr | None = None
    taskArn: StrictStr | None = None
    containers: list[BatchAttemptTaskContainerDetails] | None = None
