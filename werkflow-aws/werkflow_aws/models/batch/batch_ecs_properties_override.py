from __future__ import annotations
from pydantic import BaseModel
from .batch_task_properties_override import BatchTaskPropertiesOverride


class BatchEcsPropertiesOverride(BaseModel):
    taskProperties: list[BatchTaskPropertiesOverride] | None = None
