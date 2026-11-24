from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TransferUpdateConnectorVpcLatticeEgressConfig(BaseModel):
    ResourceConfigurationArn: StrictStr | None = None
    PortNumber: StrictInt | None = None
