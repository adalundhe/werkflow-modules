from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_cspm_connector_summary import SecurityHubCspmConnectorSummary


class SecurityHubListConnectorsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Connectors: list[SecurityHubCspmConnectorSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
