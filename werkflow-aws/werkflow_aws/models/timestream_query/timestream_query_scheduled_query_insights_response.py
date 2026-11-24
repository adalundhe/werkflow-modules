from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .timestream_query_query_spatial_coverage import TimestreamQueryQuerySpatialCoverage
from .timestream_query_query_temporal_range import TimestreamQueryQueryTemporalRange


class TimestreamQueryScheduledQueryInsightsResponse(BaseModel):
    QuerySpatialCoverage: TimestreamQueryQuerySpatialCoverage | None = None
    QueryTemporalRange: TimestreamQueryQueryTemporalRange | None = None
    QueryTableCount: StrictInt | None = None
    OutputRows: StrictInt | None = None
    OutputBytes: StrictInt | None = None
