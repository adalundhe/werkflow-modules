from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_processor import CloudWatchLogsProcessor


class CloudWatchLogsTestTransformerRequest(BaseModel):
    transformerConfig: list[CloudWatchLogsProcessor]
    logEventMessages: list[StrictStr]
