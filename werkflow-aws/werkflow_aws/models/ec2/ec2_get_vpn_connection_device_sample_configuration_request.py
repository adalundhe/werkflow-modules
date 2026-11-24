from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetVpnConnectionDeviceSampleConfigurationRequest(BaseModel):
    VpnConnectionId: StrictStr
    VpnConnectionDeviceTypeId: StrictStr
    InternetKeyExchangeVersion: StrictStr | None = None
    SampleType: StrictStr | None = None
    DryRun: StrictBool | None = None
