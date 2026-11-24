from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTProvisioningHook(BaseModel):
    payloadVersion: StrictStr | None = None
    targetArn: StrictStr | None = None
