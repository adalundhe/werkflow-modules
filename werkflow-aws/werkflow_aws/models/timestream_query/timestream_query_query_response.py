from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .timestream_query_column_info import TimestreamQueryColumnInfo
from .timestream_query_query_insights_response import TimestreamQueryQueryInsightsResponse
from .timestream_query_query_status import TimestreamQueryQueryStatus
from .timestream_query_row import TimestreamQueryRow


class TimestreamQueryQueryResponse(BaseModel):
    QueryId: StrictStr | None = None
    NextToken: StrictStr | None = None
    Rows: list[TimestreamQueryRow] | None = None
    ColumnInfo: list[TimestreamQueryColumnInfo] | None = None
    QueryStatus: TimestreamQueryQueryStatus | None = None
    QueryInsightsResponse: TimestreamQueryQueryInsightsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
