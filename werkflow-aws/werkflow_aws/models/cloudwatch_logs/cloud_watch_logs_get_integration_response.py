from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_integration_details import CloudWatchLogsIntegrationDetails


class CloudWatchLogsGetIntegrationResponse(BaseModel):
    integrationName: StrictStr | None = None
    integrationType: StrictStr | None = None
    integrationStatus: StrictStr | None = None
    integrationDetails: CloudWatchLogsIntegrationDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
