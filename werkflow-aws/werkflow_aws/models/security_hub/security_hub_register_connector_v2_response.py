from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubRegisterConnectorV2Response(BaseModel):
    ConnectorArn: StrictStr | None = None
    ConnectorId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
