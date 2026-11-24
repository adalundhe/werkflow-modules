from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetIntegrationRequest(BaseModel):
    integrationName: StrictStr
