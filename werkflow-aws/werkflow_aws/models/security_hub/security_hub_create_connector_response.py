from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubCreateConnectorResponse(BaseModel):
    ConnectorArn: StrictStr | None = None
    ConnectorId: StrictStr | None = None
    ConnectorStatus: StrictStr | None = None
    EnablementStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
