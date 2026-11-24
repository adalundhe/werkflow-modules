from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeClusterNodeRequest(BaseModel):
    ClusterName: StrictStr
    NodeId: StrictStr | None = None
    NodeLogicalId: StrictStr | None = None
