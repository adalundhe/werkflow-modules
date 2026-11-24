from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .timestream_query_scheduled_query_description import TimestreamQueryScheduledQueryDescription


class TimestreamQueryDescribeScheduledQueryResponse(BaseModel):
    ScheduledQuery: TimestreamQueryScheduledQueryDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
