from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .redshift_aqua_configuration import RedshiftAquaConfiguration
from .redshift_cluster_iam_role import RedshiftClusterIamRole
from .redshift_cluster_node import RedshiftClusterNode
from .redshift_cluster_parameter_group_status import RedshiftClusterParameterGroupStatus
from .redshift_cluster_security_group_membership import RedshiftClusterSecurityGroupMembership
from .redshift_cluster_snapshot_copy_status import RedshiftClusterSnapshotCopyStatus
from .redshift_data_transfer_progress import RedshiftDataTransferProgress
from .redshift_deferred_maintenance_window import RedshiftDeferredMaintenanceWindow
from .redshift_elastic_ip_status import RedshiftElasticIpStatus
from .redshift_endpoint import RedshiftEndpoint
from .redshift_hsm_status import RedshiftHsmStatus
from .redshift_logging_publish_status import RedshiftLoggingPublishStatus
from .redshift_pending_modified_values import RedshiftPendingModifiedValues
from .redshift_reserved_node_exchange_status import RedshiftReservedNodeExchangeStatus
from .redshift_resize_info import RedshiftResizeInfo
from .redshift_restore_status import RedshiftRestoreStatus
from .redshift_secondary_cluster_info import RedshiftSecondaryClusterInfo
from .redshift_tag import RedshiftTag
from .redshift_vpc_security_group_membership import RedshiftVpcSecurityGroupMembership


class RedshiftCluster(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    NodeType: StrictStr | None = None
    ClusterStatus: StrictStr | None = None
    ClusterAvailabilityStatus: StrictStr | None = None
    ModifyStatus: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    DBName: StrictStr | None = None
    Endpoint: RedshiftEndpoint | None = None
    ClusterCreateTime: datetime.datetime | StrictStr | None = None
    AutomatedSnapshotRetentionPeriod: StrictInt | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    ClusterSecurityGroups: list[RedshiftClusterSecurityGroupMembership] | None = None
    VpcSecurityGroups: list[RedshiftVpcSecurityGroupMembership] | None = None
    ClusterParameterGroups: list[RedshiftClusterParameterGroupStatus] | None = None
    ClusterSubnetGroupName: StrictStr | None = None
    VpcId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    PendingModifiedValues: RedshiftPendingModifiedValues | None = None
    ClusterVersion: StrictStr | None = None
    AllowVersionUpgrade: StrictBool | None = None
    NumberOfNodes: StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
    Encrypted: StrictBool | None = None
    RestoreStatus: RedshiftRestoreStatus | None = None
    DataTransferProgress: RedshiftDataTransferProgress | None = None
    HsmStatus: RedshiftHsmStatus | None = None
    ClusterSnapshotCopyStatus: RedshiftClusterSnapshotCopyStatus | None = None
    ClusterPublicKey: StrictStr | None = None
    ClusterNodes: list[RedshiftClusterNode] | None = None
    ElasticIpStatus: RedshiftElasticIpStatus | None = None
    ClusterRevisionNumber: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
    KmsKeyId: StrictStr | None = None
    EnhancedVpcRouting: StrictBool | None = None
    IamRoles: list[RedshiftClusterIamRole] | None = None
    PendingActions: list[StrictStr] | None = None
    MaintenanceTrackName: StrictStr | None = None
    ElasticResizeNumberOfNodeOptions: StrictStr | None = None
    DeferredMaintenanceWindows: list[RedshiftDeferredMaintenanceWindow] | None = None
    SnapshotScheduleIdentifier: StrictStr | None = None
    SnapshotScheduleState: StrictStr | None = None
    ExpectedNextSnapshotScheduleTime: datetime.datetime | StrictStr | None = None
    ExpectedNextSnapshotScheduleTimeStatus: StrictStr | None = None
    NextMaintenanceWindowStartTime: datetime.datetime | StrictStr | None = None
    ResizeInfo: RedshiftResizeInfo | None = None
    AvailabilityZoneRelocationStatus: StrictStr | None = None
    ClusterNamespaceArn: StrictStr | None = None
    TotalStorageCapacityInMegaBytes: StrictInt | None = None
    AquaConfiguration: RedshiftAquaConfiguration | None = None
    DefaultIamRoleArn: StrictStr | None = None
    ReservedNodeExchangeStatus: RedshiftReservedNodeExchangeStatus | None = None
    CustomDomainName: StrictStr | None = None
    CustomDomainCertificateArn: StrictStr | None = None
    CustomDomainCertificateExpiryDate: datetime.datetime | StrictStr | None = None
    MasterPasswordSecretArn: StrictStr | None = None
    MasterPasswordSecretKmsKeyId: StrictStr | None = None
    IpAddressType: StrictStr | None = None
    MultiAZ: StrictStr | None = None
    MultiAZSecondary: RedshiftSecondaryClusterInfo | None = None
    LakehouseRegistrationStatus: StrictStr | None = None
    CatalogArn: StrictStr | None = None
    ExtraComputeForAutomaticOptimization: StrictStr | None = None
    LoggingPublishStatus: RedshiftLoggingPublishStatus | None = None
