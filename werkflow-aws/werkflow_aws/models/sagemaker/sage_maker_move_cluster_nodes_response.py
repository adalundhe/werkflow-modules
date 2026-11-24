from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_move_cluster_node_logical_ids_error import SageMakerMoveClusterNodeLogicalIdsError
from .sage_maker_move_cluster_nodes_error import SageMakerMoveClusterNodesError


class SageMakerMoveClusterNodesResponse(BaseModel):
    Successful: list[StrictStr] | None = None
    Failed: list[SageMakerMoveClusterNodesError] | None = None
    SuccessfulNodeLogicalIds: list[StrictStr] | None = None
    FailedNodeLogicalIds: list[SageMakerMoveClusterNodeLogicalIdsError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
