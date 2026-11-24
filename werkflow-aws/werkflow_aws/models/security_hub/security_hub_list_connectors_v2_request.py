from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubListConnectorsV2Request(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ProviderName: Literal['JIRA_CLOUD', 'SERVICENOW', 'AZURE', 'GCP'] | None = None
    ConnectorStatus: Literal['CONNECTED', 'DEGRADED', 'FAILED_TO_CONNECT', 'PENDING_AUTHORIZATION', 'PENDING_CONFIGURATION', 'UNKNOWN'] | None = None
    EnablementStatus: Literal['ENABLED', 'PENDING_ENABLEMENT', 'FAILED_TO_ENABLE', 'PENDING_UPDATE', 'FAILED_TO_UPDATE', 'PENDING_DELETION', 'FAILED_TO_DELETE'] | None = None
