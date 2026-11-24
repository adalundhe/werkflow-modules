from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .memory_db_shard_detail import MemoryDBShardDetail


class MemoryDBClusterConfiguration(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    NodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    MaintenanceWindow: StrictStr | None = None
    TopicArn: StrictStr | None = None
    Port: StrictInt | None = None
    ParameterGroupName: StrictStr | None = None
    SubnetGroupName: StrictStr | None = None
    VpcId: StrictStr | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    SnapshotWindow: StrictStr | None = None
    NumShards: StrictInt | None = None
    Shards: list[MemoryDBShardDetail] | None = None
    MultiRegionParameterGroupName: StrictStr | None = None
    MultiRegionClusterName: StrictStr | None = None
