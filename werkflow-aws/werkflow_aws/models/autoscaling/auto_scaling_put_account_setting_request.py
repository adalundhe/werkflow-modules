from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingPutAccountSettingRequest(BaseModel):
    Name: StrictStr
    Value: StrictStr
