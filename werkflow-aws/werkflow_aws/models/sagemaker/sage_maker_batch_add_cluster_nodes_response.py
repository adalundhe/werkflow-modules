from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_batch_add_cluster_nodes_error import SageMakerBatchAddClusterNodesError
from .sage_maker_node_addition_result import SageMakerNodeAdditionResult


class SageMakerBatchAddClusterNodesResponse(BaseModel):
    Successful: list[SageMakerNodeAdditionResult] | None = None
    Failed: list[SageMakerBatchAddClusterNodesError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
