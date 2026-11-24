from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DisassociateNatGatewayAddressRequest(BaseModel):
    NatGatewayId: StrictStr
    AssociationIds: list[StrictStr]
    MaxDrainDurationSeconds: StrictInt | None = None
    DryRun: StrictBool | None = None
