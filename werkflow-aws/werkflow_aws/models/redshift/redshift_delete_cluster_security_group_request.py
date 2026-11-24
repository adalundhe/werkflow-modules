from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteClusterSecurityGroupRequest(BaseModel):
    ClusterSecurityGroupName: StrictStr
