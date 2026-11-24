from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_batch_delete_cluster_node_logical_ids_error import SageMakerBatchDeleteClusterNodeLogicalIdsError
from .sage_maker_batch_delete_cluster_nodes_error import SageMakerBatchDeleteClusterNodesError


class SageMakerBatchDeleteClusterNodesResponse(BaseModel):
    Failed: list[SageMakerBatchDeleteClusterNodesError] | None = None
    Successful: list[StrictStr] | None = None
    FailedNodeLogicalIds: list[SageMakerBatchDeleteClusterNodeLogicalIdsError] | None = None
    SuccessfulNodeLogicalIds: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
