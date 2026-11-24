from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyGetBackendEnvironmentRequest(BaseModel):
    appId: StrictStr
    environmentName: StrictStr
