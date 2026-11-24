from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmUpdateDeviceInstanceRequest(BaseModel):
    arn: StrictStr
    profileArn: StrictStr | None = None
    labels: list[StrictStr] | None = None
