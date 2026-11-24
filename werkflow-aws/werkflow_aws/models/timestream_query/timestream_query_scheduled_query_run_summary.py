from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .timestream_query_error_report_location import TimestreamQueryErrorReportLocation
from .timestream_query_execution_stats import TimestreamQueryExecutionStats
from .timestream_query_scheduled_query_insights_response import TimestreamQueryScheduledQueryInsightsResponse


class TimestreamQueryScheduledQueryRunSummary(BaseModel):
    InvocationTime: datetime.datetime | StrictStr | None = None
    TriggerTime: datetime.datetime | StrictStr | None = None
    RunStatus: StrictStr | None = None
    ExecutionStats: TimestreamQueryExecutionStats | None = None
    QueryInsightsResponse: TimestreamQueryScheduledQueryInsightsResponse | None = None
    ErrorReportLocation: TimestreamQueryErrorReportLocation | None = None
    FailureReason: StrictStr | None = None
