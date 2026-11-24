from __future__ import annotations
from pydantic import BaseModel
from .timestream_query_query_temporal_range_max import TimestreamQueryQueryTemporalRangeMax


class TimestreamQueryQueryTemporalRange(BaseModel):
    Max: TimestreamQueryQueryTemporalRangeMax | None = None
