from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_global_cluster import NeptuneGlobalCluster


class NeptuneDescribeGlobalClustersResponse(BaseModel):
    Marker: StrictStr | None = None
    GlobalClusters: list[NeptuneGlobalCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
