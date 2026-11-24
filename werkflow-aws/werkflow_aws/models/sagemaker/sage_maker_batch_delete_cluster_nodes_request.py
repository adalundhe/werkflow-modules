from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBatchDeleteClusterNodesRequest(BaseModel):
    ClusterName: StrictStr
    NodeIds: list[StrictStr] | None = None
    NodeLogicalIds: list[StrictStr] | None = None
