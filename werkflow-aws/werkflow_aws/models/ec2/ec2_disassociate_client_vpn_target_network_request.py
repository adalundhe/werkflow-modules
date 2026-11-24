from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateClientVpnTargetNetworkRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    AssociationId: StrictStr
    DryRun: StrictBool | None = None
