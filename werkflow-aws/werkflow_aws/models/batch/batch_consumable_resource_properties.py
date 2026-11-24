from __future__ import annotations
from pydantic import BaseModel
from .batch_consumable_resource_requirement import BatchConsumableResourceRequirement


class BatchConsumableResourceProperties(BaseModel):
    consumableResourceList: list[BatchConsumableResourceRequirement] | None = None
