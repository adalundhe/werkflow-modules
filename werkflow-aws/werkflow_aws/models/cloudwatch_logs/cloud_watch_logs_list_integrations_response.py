from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_integration_summary import CloudWatchLogsIntegrationSummary


class CloudWatchLogsListIntegrationsResponse(BaseModel):
    integrationSummaries: list[CloudWatchLogsIntegrationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
