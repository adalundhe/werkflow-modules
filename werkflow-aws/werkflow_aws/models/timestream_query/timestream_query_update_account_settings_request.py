from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .timestream_query_query_compute_request import TimestreamQueryQueryComputeRequest


class TimestreamQueryUpdateAccountSettingsRequest(BaseModel):
    MaxQueryTCU: StrictInt | None = None
    QueryPricingModel: Literal['BYTES_SCANNED', 'COMPUTE_UNITS'] | None = None
    QueryCompute: TimestreamQueryQueryComputeRequest | None = None
