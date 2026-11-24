from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferDescribedConnectorVpcLatticeEgressConfig(BaseModel):
    ResourceConfigurationArn: StrictStr | None = None
    PortNumber: StrictInt | None = None
