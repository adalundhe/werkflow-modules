from __future__ import annotations
from pydantic import BaseModel
from .batch_ecs_task_details import BatchEcsTaskDetails


class BatchEcsPropertiesDetail(BaseModel):
    taskProperties: list[BatchEcsTaskDetails] | None = None
