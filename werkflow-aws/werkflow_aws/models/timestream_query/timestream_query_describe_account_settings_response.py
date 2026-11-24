from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .timestream_query_query_compute_response import TimestreamQueryQueryComputeResponse


class TimestreamQueryDescribeAccountSettingsResponse(BaseModel):
    MaxQueryTCU: StrictInt | None = None
    QueryPricingModel: StrictStr | None = None
    QueryCompute: TimestreamQueryQueryComputeResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
