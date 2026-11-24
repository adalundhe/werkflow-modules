from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSAssociateGatewayWithClusterRequest(BaseModel):
    gateway: StrictStr
    cluster: StrictStr
