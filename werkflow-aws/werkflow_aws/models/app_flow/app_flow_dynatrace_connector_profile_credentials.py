from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowDynatraceConnectorProfileCredentials(BaseModel):
    apiToken: StrictStr
