from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDetachClusterNodeVolumeRequest(BaseModel):
    ClusterArn: StrictStr
    NodeId: StrictStr
    VolumeId: StrictStr
