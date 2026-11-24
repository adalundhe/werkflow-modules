from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .timestream_query_error_report_configuration import TimestreamQueryErrorReportConfiguration
from .timestream_query_notification_configuration import TimestreamQueryNotificationConfiguration
from .timestream_query_schedule_configuration import TimestreamQueryScheduleConfiguration
from .timestream_query_scheduled_query_run_summary import TimestreamQueryScheduledQueryRunSummary
from .timestream_query_target_configuration import TimestreamQueryTargetConfiguration


class TimestreamQueryScheduledQueryDescription(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    QueryString: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    PreviousInvocationTime: datetime.datetime | StrictStr | None = None
    NextInvocationTime: datetime.datetime | StrictStr | None = None
    ScheduleConfiguration: TimestreamQueryScheduleConfiguration | None = None
    NotificationConfiguration: TimestreamQueryNotificationConfiguration | None = None
    TargetConfiguration: TimestreamQueryTargetConfiguration | None = None
    ScheduledQueryExecutionRoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    ErrorReportConfiguration: TimestreamQueryErrorReportConfiguration | None = None
    LastRunSummary: TimestreamQueryScheduledQueryRunSummary | None = None
    RecentlyFailedRuns: list[TimestreamQueryScheduledQueryRunSummary] | None = None
