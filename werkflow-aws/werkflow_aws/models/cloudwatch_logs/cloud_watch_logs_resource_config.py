from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_open_search_resource_config import CloudWatchLogsOpenSearchResourceConfig


class CloudWatchLogsResourceConfig(BaseModel):
    openSearchResourceConfig: CloudWatchLogsOpenSearchResourceConfig | None = None
