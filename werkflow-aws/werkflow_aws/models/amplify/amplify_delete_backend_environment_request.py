from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyDeleteBackendEnvironmentRequest(BaseModel):
    appId: StrictStr
    environmentName: StrictStr
