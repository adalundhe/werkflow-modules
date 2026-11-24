from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_batch_reboot_cluster_node_logical_ids_error import SageMakerBatchRebootClusterNodeLogicalIdsError
from .sage_maker_batch_reboot_cluster_nodes_error import SageMakerBatchRebootClusterNodesError


class SageMakerBatchRebootClusterNodesResponse(BaseModel):
    Successful: list[StrictStr] | None = None
    Failed: list[SageMakerBatchRebootClusterNodesError] | None = None
    FailedNodeLogicalIds: list[SageMakerBatchRebootClusterNodeLogicalIdsError] | None = None
    SuccessfulNodeLogicalIds: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
