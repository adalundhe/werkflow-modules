from __future__ import annotations
from pydantic import BaseModel
from .batch_ecs_task_properties import BatchEcsTaskProperties


class BatchEcsProperties(BaseModel):
    taskProperties: list[BatchEcsTaskProperties] | None = None
