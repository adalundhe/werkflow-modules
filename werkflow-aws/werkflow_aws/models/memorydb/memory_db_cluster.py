from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .memory_db_cluster_pending_updates import MemoryDBClusterPendingUpdates
from .memory_db_endpoint import MemoryDBEndpoint
from .memory_db_security_group_membership import MemoryDBSecurityGroupMembership
from .memory_db_shard import MemoryDBShard


class MemoryDBCluster(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    PendingUpdates: MemoryDBClusterPendingUpdates | None = None
    MultiRegionClusterName: StrictStr | None = None
    NumberOfShards: StrictInt | None = None
    Shards: list[MemoryDBShard] | None = None
    AvailabilityMode: StrictStr | None = None
    ClusterEndpoint: MemoryDBEndpoint | None = None
    NodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    EnginePatchVersion: StrictStr | None = None
    ParameterGroupName: StrictStr | None = None
    ParameterGroupStatus: StrictStr | None = None
    SecurityGroups: list[MemoryDBSecurityGroupMembership] | None = None
    SubnetGroupName: StrictStr | None = None
    TLSEnabled: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    ARN: StrictStr | None = None
    SnsTopicArn: StrictStr | None = None
    SnsTopicStatus: StrictStr | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    MaintenanceWindow: StrictStr | None = None
    SnapshotWindow: StrictStr | None = None
    ACLName: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    DataTiering: StrictStr | None = None
    NetworkType: StrictStr | None = None
    IpDiscovery: StrictStr | None = None
