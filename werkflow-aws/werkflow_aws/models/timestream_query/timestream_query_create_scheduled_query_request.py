from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_query_error_report_configuration import TimestreamQueryErrorReportConfiguration
from .timestream_query_notification_configuration import TimestreamQueryNotificationConfiguration
from .timestream_query_schedule_configuration import TimestreamQueryScheduleConfiguration
from .timestream_query_tag import TimestreamQueryTag
from .timestream_query_target_configuration import TimestreamQueryTargetConfiguration


class TimestreamQueryCreateScheduledQueryRequest(BaseModel):
    Name: StrictStr
    QueryString: StrictStr
    ScheduleConfiguration: TimestreamQueryScheduleConfiguration
    NotificationConfiguration: TimestreamQueryNotificationConfiguration
    ScheduledQueryExecutionRoleArn: StrictStr
    ErrorReportConfiguration: TimestreamQueryErrorReportConfiguration
    TargetConfiguration: TimestreamQueryTargetConfiguration | None = None
    ClientToken: StrictStr | None = None
    Tags: list[TimestreamQueryTag] | None = None
    KmsKeyId: StrictStr | None = None
