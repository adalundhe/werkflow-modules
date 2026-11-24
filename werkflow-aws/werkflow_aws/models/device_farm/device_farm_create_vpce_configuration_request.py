from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmCreateVPCEConfigurationRequest(BaseModel):
    vpceConfigurationName: StrictStr
    vpceServiceName: StrictStr
    serviceDnsName: StrictStr
    vpceConfigurationDescription: StrictStr | None = None
