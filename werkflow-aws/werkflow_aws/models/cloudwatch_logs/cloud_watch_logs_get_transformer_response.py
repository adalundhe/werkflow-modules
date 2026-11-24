from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_processor import CloudWatchLogsProcessor


class CloudWatchLogsGetTransformerResponse(BaseModel):
    logGroupIdentifier: StrictStr | None = None
    creationTime: StrictInt | None = None
    lastModifiedTime: StrictInt | None = None
    transformerConfig: list[CloudWatchLogsProcessor] | None = None
    ResponseMetadata: dict[str, Any] | None = None
