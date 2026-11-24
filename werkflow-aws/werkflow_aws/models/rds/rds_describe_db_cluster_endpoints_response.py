from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_cluster_endpoint import RDSDBClusterEndpoint


class RDSDescribeDBClusterEndpointsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterEndpoints: list[RDSDBClusterEndpoint] | None = None
    ResponseMetadata: dict[str, Any] | None = None
