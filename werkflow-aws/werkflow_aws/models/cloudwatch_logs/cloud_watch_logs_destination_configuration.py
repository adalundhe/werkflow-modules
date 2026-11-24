from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_lookup_table_configuration import CloudWatchLogsLookupTableConfiguration
from .cloud_watch_logs_s3_configuration import CloudWatchLogsS3Configuration


class CloudWatchLogsDestinationConfiguration(BaseModel):
    s3Configuration: CloudWatchLogsS3Configuration | None = None
    lookupTableConfiguration: CloudWatchLogsLookupTableConfiguration | None = None
