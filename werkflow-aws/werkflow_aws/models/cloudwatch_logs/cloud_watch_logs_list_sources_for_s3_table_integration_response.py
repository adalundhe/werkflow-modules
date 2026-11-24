from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_s3_table_integration_source import CloudWatchLogsS3TableIntegrationSource


class CloudWatchLogsListSourcesForS3TableIntegrationResponse(BaseModel):
    sources: list[CloudWatchLogsS3TableIntegrationSource] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
