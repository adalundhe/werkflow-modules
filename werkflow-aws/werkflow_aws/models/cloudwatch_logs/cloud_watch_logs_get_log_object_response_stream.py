from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_fields_data import CloudWatchLogsFieldsData
from .cloud_watch_logs_internal_streaming_exception import CloudWatchLogsInternalStreamingException


class CloudWatchLogsGetLogObjectResponseStream(BaseModel):
    fields: CloudWatchLogsFieldsData | None = None
    InternalStreamingException: CloudWatchLogsInternalStreamingException | None = None
