from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetConnectorV2Request(BaseModel):
    ConnectorId: StrictStr
