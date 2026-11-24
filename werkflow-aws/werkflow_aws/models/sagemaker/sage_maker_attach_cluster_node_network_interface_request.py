from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAttachClusterNodeNetworkInterfaceRequest(BaseModel):
    ClusterName: StrictStr
    NodeId: StrictStr
    NetworkInterfaceId: StrictStr
