from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSnowflakeConnectorProfileCredentials(BaseModel):
    username: StrictStr
    password: StrictStr | None = None
    privateKey: StrictStr | None = None
