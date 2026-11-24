from __future__ import annotations
from pydantic import BaseModel
from .timestream_query_timestream_configuration import TimestreamQueryTimestreamConfiguration


class TimestreamQueryTargetConfiguration(BaseModel):
    TimestreamConfiguration: TimestreamQueryTimestreamConfiguration | None = None
