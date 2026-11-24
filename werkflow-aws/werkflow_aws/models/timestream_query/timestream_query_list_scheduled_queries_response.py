from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .timestream_query_scheduled_query import TimestreamQueryScheduledQuery


class TimestreamQueryListScheduledQueriesResponse(BaseModel):
    ScheduledQueries: list[TimestreamQueryScheduledQuery] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
