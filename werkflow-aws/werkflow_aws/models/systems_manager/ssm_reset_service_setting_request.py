from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMResetServiceSettingRequest(BaseModel):
    SettingId: StrictStr
