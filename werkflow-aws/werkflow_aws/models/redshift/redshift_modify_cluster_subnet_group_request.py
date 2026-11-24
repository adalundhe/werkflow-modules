from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftModifyClusterSubnetGroupRequest(BaseModel):
    ClusterSubnetGroupName: StrictStr
    SubnetIds: list[StrictStr]
    Description: StrictStr | None = None
