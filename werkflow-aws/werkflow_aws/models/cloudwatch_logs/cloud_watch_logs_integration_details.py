from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_open_search_integration_details import CloudWatchLogsOpenSearchIntegrationDetails


class CloudWatchLogsIntegrationDetails(BaseModel):
    openSearchIntegrationDetails: CloudWatchLogsOpenSearchIntegrationDetails | None = None
