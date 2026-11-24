from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .timestream_query_query_insights import TimestreamQueryQueryInsights


class TimestreamQueryQueryRequest(BaseModel):
    QueryString: StrictStr
    ClientToken: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxRows: StrictInt | None = None
    QueryInsights: TimestreamQueryQueryInsights | None = None
