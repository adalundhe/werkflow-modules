from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_cluster_master_user_secret import DocumentDBClusterMasterUserSecret
from .document_dbdb_cluster_member import DocumentDBDBClusterMember
from .document_dbdb_cluster_role import DocumentDBDBClusterRole
from .document_db_serverless_v2_scaling_configuration_info import DocumentDBServerlessV2ScalingConfigurationInfo
from .document_db_vpc_security_group_membership import DocumentDBVpcSecurityGroupMembership


class DocumentDBDBCluster(BaseModel):
    AvailabilityZones: list[StrictStr] | None = None
    BackupRetentionPeriod: StrictInt | None = None
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
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    ReplicationSourceIdentifier: StrictStr | None = None
    ReadReplicaIdentifiers: list[StrictStr] | None = None
    DBClusterMembers: list[DocumentDBDBClusterMember] | None = None
    VpcSecurityGroups: list[DocumentDBVpcSecurityGroupMembership] | None = None
    HostedZoneId: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DbClusterResourceId: StrictStr | None = None
    DBClusterArn: StrictStr | None = None
    AssociatedRoles: list[DocumentDBDBClusterRole] | None = None
    CloneGroupId: StrictStr | None = None
    ClusterCreateTime: datetime.datetime | StrictStr | None = None
    EnabledCloudwatchLogsExports: list[StrictStr] | None = None
    DeletionProtection: StrictBool | None = None
    IOOptimizedNextAllowedModificationTime: datetime.datetime | StrictStr | None = None
    StorageType: StrictStr | None = None
    ServerlessV2ScalingConfiguration: DocumentDBServerlessV2ScalingConfigurationInfo | None = None
    ServerlessV2PlatformVersion: StrictStr | None = None
    MasterUserSecret: DocumentDBClusterMasterUserSecret | None = None
    NetworkType: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
