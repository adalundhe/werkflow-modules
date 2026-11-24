from __future__ import annotations
from pydantic import BaseModel
from .timestream_query_query_spatial_coverage_max import TimestreamQueryQuerySpatialCoverageMax


class TimestreamQueryQuerySpatialCoverage(BaseModel):
    Max: TimestreamQueryQuerySpatialCoverageMax | None = None
