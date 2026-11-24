from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_type_converter_entry import CloudWatchLogsTypeConverterEntry


class CloudWatchLogsTypeConverter(BaseModel):
    entries: list[CloudWatchLogsTypeConverterEntry] | None = None
