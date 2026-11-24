from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferConnectorVpcLatticeEgressConfig(BaseModel):
    ResourceConfigurationArn: StrictStr
    PortNumber: StrictInt | None = None
