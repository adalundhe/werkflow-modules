from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_node_summary import SageMakerClusterNodeSummary


class SageMakerListClusterNodesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ClusterNodeSummaries: list[SageMakerClusterNodeSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
