from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRegisterConnectorV2Request(BaseModel):
    AuthCode: StrictStr
    AuthState: StrictStr
