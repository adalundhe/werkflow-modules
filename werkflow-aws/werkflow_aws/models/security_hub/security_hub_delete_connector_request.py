from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteConnectorRequest(BaseModel):
    ConnectorId: StrictStr
