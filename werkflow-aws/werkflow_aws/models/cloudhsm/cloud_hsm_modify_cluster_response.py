from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_hsm_cluster import CloudHSMCluster


class CloudHSMModifyClusterResponse(BaseModel):
    Cluster: CloudHSMCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
