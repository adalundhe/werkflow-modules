from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowAmplitudeConnectorProfileCredentials(BaseModel):
    apiKey: StrictStr
    secretKey: StrictStr
