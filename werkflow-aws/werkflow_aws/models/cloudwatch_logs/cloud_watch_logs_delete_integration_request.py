from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsDeleteIntegrationRequest(BaseModel):
    integrationName: StrictStr
    force: StrictBool | None = None
