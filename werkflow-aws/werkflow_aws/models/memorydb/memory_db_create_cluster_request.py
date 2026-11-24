from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBCreateClusterRequest(BaseModel):
    ClusterName: StrictStr
    NodeType: StrictStr
    ACLName: StrictStr
    MultiRegionClusterName: StrictStr | None = None
    ParameterGroupName: StrictStr | None = None
    Description: StrictStr | None = None
    NumShards: StrictInt | None = None
    NumReplicasPerShard: StrictInt | None = None
    SubnetGroupName: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    MaintenanceWindow: StrictStr | None = None
    Port: StrictInt | None = None
    SnsTopicArn: StrictStr | None = None
    TLSEnabled: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    SnapshotArns: list[StrictStr] | None = None
    SnapshotName: StrictStr | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    Tags: list[MemoryDBTag] | None = None
    SnapshotWindow: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    DataTiering: StrictBool | None = None
    NetworkType: Literal['ipv4', 'ipv6', 'dual_stack'] | None = None
    IpDiscovery: Literal['ipv4', 'ipv6'] | None = None
