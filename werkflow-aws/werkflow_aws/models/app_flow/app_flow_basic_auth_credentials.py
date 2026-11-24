from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowBasicAuthCredentials(BaseModel):
    username: StrictStr
    password: StrictStr
