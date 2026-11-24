from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .timestream_query_scheduled_query_insights import TimestreamQueryScheduledQueryInsights


class TimestreamQueryExecuteScheduledQueryRequest(BaseModel):
    ScheduledQueryArn: StrictStr
    InvocationTime: datetime.datetime | StrictStr
    ClientToken: StrictStr | None = None
    QueryInsights: TimestreamQueryScheduledQueryInsights | None = None
