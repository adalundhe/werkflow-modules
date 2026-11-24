from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_list_jobs_by_consumable_resource_summary import BatchListJobsByConsumableResourceSummary


class BatchListJobsByConsumableResourceResponse(BaseModel):
    jobs: list[BatchListJobsByConsumableResourceSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
