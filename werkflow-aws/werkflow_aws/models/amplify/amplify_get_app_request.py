from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyGetAppRequest(BaseModel):
    appId: StrictStr
