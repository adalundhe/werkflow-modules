from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPutAccountSettingRequest(BaseModel):
    name: StrictStr
    value: StrictStr
