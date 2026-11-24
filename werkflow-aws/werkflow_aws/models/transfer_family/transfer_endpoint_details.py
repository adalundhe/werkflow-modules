from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferEndpointDetails(BaseModel):
    AddressAllocationIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
    VpcEndpointId: StrictStr | None = None
    VpcId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
