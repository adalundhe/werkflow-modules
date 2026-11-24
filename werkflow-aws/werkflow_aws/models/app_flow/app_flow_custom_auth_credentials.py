from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowCustomAuthCredentials(BaseModel):
    customAuthenticationType: StrictStr
    credentialsMap: dict[StrictStr, StrictStr] | None = None
