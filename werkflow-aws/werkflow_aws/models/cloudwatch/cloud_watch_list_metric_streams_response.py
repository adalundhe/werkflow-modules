from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_metric_stream_entry import CloudWatchMetricStreamEntry


class CloudWatchListMetricStreamsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Entries: list[CloudWatchMetricStreamEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
