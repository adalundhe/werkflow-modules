from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .io_t_bucket import IoTBucket


class IoTGetBucketsAggregationResponse(BaseModel):
    totalCount: StrictInt | None = None
    buckets: list[IoTBucket] | None = None
    ResponseMetadata: dict[str, Any] | None = None
