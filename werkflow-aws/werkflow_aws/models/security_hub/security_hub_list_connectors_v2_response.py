from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_connector_summary import SecurityHubConnectorSummary


class SecurityHubListConnectorsV2Response(BaseModel):
    NextToken: StrictStr | None = None
    Connectors: list[SecurityHubConnectorSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
