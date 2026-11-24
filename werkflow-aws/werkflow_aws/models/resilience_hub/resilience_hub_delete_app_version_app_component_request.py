from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDeleteAppVersionAppComponentRequest(BaseModel):
    appArn: StrictStr
    id: StrictStr
    clientToken: StrictStr | None = None
