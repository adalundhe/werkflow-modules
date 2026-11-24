from __future__ import annotations
from pydantic import BaseModel
from .kinesis_cloud_watch_logs import KinesisCloudWatchLogs


class KinesisChannelLoggingConfiguration(BaseModel):
    CloudWatchLogs: KinesisCloudWatchLogs | None = None
