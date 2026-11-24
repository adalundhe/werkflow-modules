from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .timestream_query_error_report_configuration import TimestreamQueryErrorReportConfiguration
from .timestream_query_target_destination import TimestreamQueryTargetDestination


class TimestreamQueryScheduledQuery(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    PreviousInvocationTime: datetime.datetime | StrictStr | None = None
    NextInvocationTime: datetime.datetime | StrictStr | None = None
    ErrorReportConfiguration: TimestreamQueryErrorReportConfiguration | None = None
    TargetDestination: TimestreamQueryTargetDestination | None = None
    LastRunStatus: StrictStr | None = None
