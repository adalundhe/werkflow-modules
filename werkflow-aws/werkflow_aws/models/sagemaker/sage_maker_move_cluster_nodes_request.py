from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerMoveClusterNodesRequest(BaseModel):
    SourceClusterArn: StrictStr
    SourceInstanceGroupName: StrictStr
    TargetClusterArn: StrictStr
    TargetInstanceGroupName: StrictStr
    InstanceCount: StrictInt | None = None
    NodeIds: list[StrictStr] | None = None
    NodeLogicalIds: list[StrictStr] | None = None
    ClientToken: StrictStr | None = None
