from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKRejectClientVpcConnectionRequest(BaseModel):
    ClusterArn: StrictStr
    VpcConnectionArn: StrictStr
