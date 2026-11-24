from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmDeleteVPCEConfigurationRequest(BaseModel):
    arn: StrictStr
