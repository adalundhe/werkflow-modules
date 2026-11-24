from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftResizeClusterRequest(BaseModel):
    ClusterIdentifier: StrictStr
    ClusterType: StrictStr | None = None
    NodeType: StrictStr | None = None
    NumberOfNodes: StrictInt | None = None
    Classic: StrictBool | None = None
    ReservedNodeId: StrictStr | None = None
    TargetReservedNodeOfferingId: StrictStr | None = None
