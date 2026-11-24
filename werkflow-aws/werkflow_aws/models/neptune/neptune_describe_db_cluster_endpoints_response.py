from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_db_cluster_endpoint import NeptuneDBClusterEndpoint


class NeptuneDescribeDBClusterEndpointsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterEndpoints: list[NeptuneDBClusterEndpoint] | None = None
    ResponseMetadata: dict[str, Any] | None = None
