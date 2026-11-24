from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_consumable_resource_summary import BatchConsumableResourceSummary


class BatchListConsumableResourcesResponse(BaseModel):
    consumableResources: list[BatchConsumableResourceSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
