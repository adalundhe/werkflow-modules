from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetConnectorRequest(BaseModel):
    ConnectorId: StrictStr
