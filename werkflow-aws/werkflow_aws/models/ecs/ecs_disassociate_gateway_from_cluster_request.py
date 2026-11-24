from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDisassociateGatewayFromClusterRequest(BaseModel):
    gateway: StrictStr
    cluster: StrictStr
