from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowDatadogConnectorProfileCredentials(BaseModel):
    apiKey: StrictStr
    applicationKey: StrictStr
