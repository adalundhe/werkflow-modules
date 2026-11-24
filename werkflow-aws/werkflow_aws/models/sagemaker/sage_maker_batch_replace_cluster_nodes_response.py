from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_batch_replace_cluster_node_logical_ids_error import SageMakerBatchReplaceClusterNodeLogicalIdsError
from .sage_maker_batch_replace_cluster_nodes_error import SageMakerBatchReplaceClusterNodesError


class SageMakerBatchReplaceClusterNodesResponse(BaseModel):
    Successful: list[StrictStr] | None = None
    Failed: list[SageMakerBatchReplaceClusterNodesError] | None = None
    FailedNodeLogicalIds: list[SageMakerBatchReplaceClusterNodeLogicalIdsError] | None = None
    SuccessfulNodeLogicalIds: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
