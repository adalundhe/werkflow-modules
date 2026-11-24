from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_cluster_pending_modified_values import NeptuneClusterPendingModifiedValues
from .neptune_db_cluster_member import NeptuneDBClusterMember
from .neptune_db_cluster_option_group_status import NeptuneDBClusterOptionGroupStatus
from .neptune_db_cluster_role import NeptuneDBClusterRole
from .neptune_serverless_v2_scaling_configuration_info import NeptuneServerlessV2ScalingConfigurationInfo
from .neptune_vpc_security_group_membership import NeptuneVpcSecurityGroupMembership


class NeptuneDBCluster(BaseModel):
    AllocatedStorage: StrictInt | None = None
    AvailabilityZones: list[StrictStr] | None = None
    BackupRetentionPeriod: StrictInt | None = None
    CharacterSetName: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    DBClusterIdentifier: StrictStr | None = None
    DBClusterParameterGroup: StrictStr | None = None
    DBSubnetGroup: StrictStr | None = None
    Status: StrictStr | None = None
    PercentProgress: StrictStr | None = None
    EarliestRestorableTime: datetime.datetime | StrictStr | None = None
    Endpoint: StrictStr | None = None
    ReaderEndpoint: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LatestRestorableTime: datetime.datetime | StrictStr | None = None
    Port: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    DBClusterOptionGroupMemberships: list[NeptuneDBClusterOptionGroupStatus] | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    ReplicationSourceIdentifier: StrictStr | None = None
    ReadReplicaIdentifiers: list[StrictStr] | None = None
    DBClusterMembers: list[NeptuneDBClusterMember] | None = None
    VpcSecurityGroups: list[NeptuneVpcSecurityGroupMembership] | None = None
    HostedZoneId: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DbClusterResourceId: StrictStr | None = None
    DBClusterArn: StrictStr | None = None
    AssociatedRoles: list[NeptuneDBClusterRole] | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    CloneGroupId: StrictStr | None = None
    ClusterCreateTime: datetime.datetime | StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    EnabledCloudwatchLogsExports: list[StrictStr] | None = None
    PendingModifiedValues: NeptuneClusterPendingModifiedValues | None = None
    DeletionProtection: StrictBool | None = None
    CrossAccountClone: StrictBool | None = None
    AutomaticRestartTime: datetime.datetime | StrictStr | None = None
    ServerlessV2ScalingConfiguration: NeptuneServerlessV2ScalingConfigurationInfo | None = None
    ServerlessV2PlatformVersion: StrictStr | None = None
    GlobalClusterIdentifier: StrictStr | None = None
    IOOptimizedNextAllowedModificationTime: datetime.datetime | StrictStr | None = None
    StorageType: StrictStr | None = None
    NetworkType: StrictStr | None = None
