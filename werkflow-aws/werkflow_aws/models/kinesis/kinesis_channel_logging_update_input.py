from __future__ import annotations
from pydantic import BaseModel
from .kinesis_cloud_watch_logs_update_input import KinesisCloudWatchLogsUpdateInput


class KinesisChannelLoggingUpdateInput(BaseModel):
    CloudWatchLogs: KinesisCloudWatchLogsUpdateInput
