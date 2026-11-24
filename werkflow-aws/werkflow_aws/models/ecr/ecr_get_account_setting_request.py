from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRGetAccountSettingRequest(BaseModel):
    name: StrictStr
