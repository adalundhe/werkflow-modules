from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateClientVpnTargetNetworkRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    SubnetId: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
