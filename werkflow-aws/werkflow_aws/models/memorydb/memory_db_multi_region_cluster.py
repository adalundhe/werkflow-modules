from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .memory_db_regional_cluster import MemoryDBRegionalCluster


class MemoryDBMultiRegionCluster(BaseModel):
    MultiRegionClusterName: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    NodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    NumberOfShards: StrictInt | None = None
    Clusters: list[MemoryDBRegionalCluster] | None = None
    MultiRegionParameterGroupName: StrictStr | None = None
    TLSEnabled: StrictBool | None = None
    ARN: StrictStr | None = None
