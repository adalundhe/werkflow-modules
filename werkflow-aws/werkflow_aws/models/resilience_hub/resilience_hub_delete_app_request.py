from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ResilienceHubDeleteAppRequest(BaseModel):
    appArn: StrictStr
    clientToken: StrictStr | None = None
    forceDelete: StrictBool | None = None
