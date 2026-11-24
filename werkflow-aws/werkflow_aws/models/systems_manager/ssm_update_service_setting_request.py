from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMUpdateServiceSettingRequest(BaseModel):
    SettingId: StrictStr
    SettingValue: StrictStr
