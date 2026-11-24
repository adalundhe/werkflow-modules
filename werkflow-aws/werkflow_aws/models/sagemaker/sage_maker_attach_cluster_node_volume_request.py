from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAttachClusterNodeVolumeRequest(BaseModel):
    ClusterArn: StrictStr
    NodeId: StrictStr
    VolumeId: StrictStr
