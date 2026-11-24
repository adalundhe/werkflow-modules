from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsIntegrationSummary(BaseModel):
    integrationName: StrictStr | None = None
    integrationType: StrictStr | None = None
    integrationStatus: StrictStr | None = None
