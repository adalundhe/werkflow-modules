from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ExportClientVpnClientConfigurationRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    DryRun: StrictBool | None = None
