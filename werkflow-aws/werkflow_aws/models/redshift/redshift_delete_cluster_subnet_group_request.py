from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteClusterSubnetGroupRequest(BaseModel):
    ClusterSubnetGroupName: StrictStr
