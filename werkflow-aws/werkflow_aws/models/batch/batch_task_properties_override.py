from __future__ import annotations
from pydantic import BaseModel
from .batch_task_container_overrides import BatchTaskContainerOverrides


class BatchTaskPropertiesOverride(BaseModel):
    containers: list[BatchTaskContainerOverrides] | None = None
