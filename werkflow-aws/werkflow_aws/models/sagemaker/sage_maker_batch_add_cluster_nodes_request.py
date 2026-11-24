from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_add_cluster_node_specification import SageMakerAddClusterNodeSpecification


class SageMakerBatchAddClusterNodesRequest(BaseModel):
    ClusterName: StrictStr
    NodesToAdd: list[SageMakerAddClusterNodeSpecification]
    ClientToken: StrictStr | None = None
