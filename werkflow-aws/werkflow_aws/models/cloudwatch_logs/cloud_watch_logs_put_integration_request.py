from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_resource_config import CloudWatchLogsResourceConfig


class CloudWatchLogsPutIntegrationRequest(BaseModel):
    integrationName: StrictStr
    resourceConfig: CloudWatchLogsResourceConfig
    integrationType: Literal['OPENSEARCH']
