from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowVeevaConnectorProfileCredentials(BaseModel):
    username: StrictStr
    password: StrictStr
