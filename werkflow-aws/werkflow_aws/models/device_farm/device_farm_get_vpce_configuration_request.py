from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetVPCEConfigurationRequest(BaseModel):
    arn: StrictStr
