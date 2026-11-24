from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_processor import CloudWatchLogsProcessor


class CloudWatchLogsPutTransformerRequest(BaseModel):
    logGroupIdentifier: StrictStr
    transformerConfig: list[CloudWatchLogsProcessor]
