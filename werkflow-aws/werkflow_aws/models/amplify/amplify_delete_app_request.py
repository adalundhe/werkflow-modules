from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyDeleteAppRequest(BaseModel):
    appId: StrictStr
