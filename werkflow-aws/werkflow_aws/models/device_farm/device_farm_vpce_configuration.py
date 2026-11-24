from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmVPCEConfiguration(BaseModel):
    arn: StrictStr | None = None
    vpceConfigurationName: StrictStr | None = None
    vpceServiceName: StrictStr | None = None
    serviceDnsName: StrictStr | None = None
    vpceConfigurationDescription: StrictStr | None = None
