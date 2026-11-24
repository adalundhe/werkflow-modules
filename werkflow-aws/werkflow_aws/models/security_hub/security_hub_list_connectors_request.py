from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubListConnectorsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ProviderName: Literal['AZURE', 'GCP'] | None = None
    ConnectorStatus: Literal['CONNECTED', 'DEGRADED', 'FAILED_TO_CONNECT', 'UNKNOWN'] | None = None
    EnablementStatus: Literal['ENABLED', 'PENDING_ENABLEMENT', 'PENDING_UPDATE', 'PENDING_DELETION'] | None = None
