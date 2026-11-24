from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBatchReplaceClusterNodesRequest(BaseModel):
    ClusterName: StrictStr
    NodeIds: list[StrictStr] | None = None
    NodeLogicalIds: list[StrictStr] | None = None
