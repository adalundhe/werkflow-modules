from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribedWebAppVpcConfig(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
