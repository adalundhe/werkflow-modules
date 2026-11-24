from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetServiceSettingRequest(BaseModel):
    SettingId: StrictStr
