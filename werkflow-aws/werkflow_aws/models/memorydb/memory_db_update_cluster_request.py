from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .memory_db_replica_configuration_request import MemoryDBReplicaConfigurationRequest
from .memory_db_shard_configuration_request import MemoryDBShardConfigurationRequest


class MemoryDBUpdateClusterRequest(BaseModel):
    ClusterName: StrictStr
    Description: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    MaintenanceWindow: StrictStr | None = None
    SnsTopicArn: StrictStr | None = None
    SnsTopicStatus: StrictStr | None = None
    ParameterGroupName: StrictStr | None = None
    SnapshotWindow: StrictStr | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    NodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    ReplicaConfiguration: MemoryDBReplicaConfigurationRequest | None = None
    ShardConfiguration: MemoryDBShardConfigurationRequest | None = None
    ACLName: StrictStr | None = None
    IpDiscovery: Literal['ipv4', 'ipv6'] | None = None
