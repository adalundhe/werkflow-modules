from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_cluster_node_details import SageMakerClusterNodeDetails


class SageMakerDescribeClusterNodeResponse(BaseModel):
    NodeDetails: SageMakerClusterNodeDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
