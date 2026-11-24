from __future__ import annotations
from pydantic import BaseModel
from .timestream_query_timestream_destination import TimestreamQueryTimestreamDestination


class TimestreamQueryTargetDestination(BaseModel):
    TimestreamDestination: TimestreamQueryTimestreamDestination | None = None
