from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_log_field_type import CloudWatchLogsLogFieldType


class CloudWatchLogsLogFieldsListItem(BaseModel):
    logFieldName: StrictStr | None = None
    logFieldType: CloudWatchLogsLogFieldType | None = None
