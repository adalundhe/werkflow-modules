from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteConnectorV2Request(BaseModel):
    ConnectorId: StrictStr
