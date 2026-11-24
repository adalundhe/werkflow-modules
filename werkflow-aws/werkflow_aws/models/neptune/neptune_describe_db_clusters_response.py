from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_db_cluster import NeptuneDBCluster


class NeptuneDescribeDBClustersResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusters: list[NeptuneDBCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
