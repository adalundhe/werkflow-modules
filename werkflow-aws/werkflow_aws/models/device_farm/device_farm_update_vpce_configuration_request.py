from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmUpdateVPCEConfigurationRequest(BaseModel):
    arn: StrictStr
    vpceConfigurationName: StrictStr | None = None
    vpceServiceName: StrictStr | None = None
    serviceDnsName: StrictStr | None = None
    vpceConfigurationDescription: StrictStr | None = None
