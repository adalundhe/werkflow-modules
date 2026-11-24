from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudWatchLogsListIntegrationsRequest(BaseModel):
    integrationNamePrefix: StrictStr | None = None
    integrationType: Literal['OPENSEARCH'] | None = None
    integrationStatus: Literal['PROVISIONING', 'ACTIVE', 'FAILED'] | None = None
