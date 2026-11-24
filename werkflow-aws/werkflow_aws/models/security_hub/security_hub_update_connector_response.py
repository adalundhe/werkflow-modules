from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubUpdateConnectorResponse(BaseModel):
    ConnectorStatus: StrictStr | None = None
    EnablementStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
