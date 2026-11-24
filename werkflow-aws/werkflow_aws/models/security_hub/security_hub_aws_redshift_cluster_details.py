from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_redshift_cluster_cluster_node import SecurityHubAwsRedshiftClusterClusterNode
from .security_hub_aws_redshift_cluster_cluster_parameter_group import SecurityHubAwsRedshiftClusterClusterParameterGroup
from .security_hub_aws_redshift_cluster_cluster_security_group import SecurityHubAwsRedshiftClusterClusterSecurityGroup
from .security_hub_aws_redshift_cluster_cluster_snapshot_copy_status import SecurityHubAwsRedshiftClusterClusterSnapshotCopyStatus
from .security_hub_aws_redshift_cluster_deferred_maintenance_window import SecurityHubAwsRedshiftClusterDeferredMaintenanceWindow
from .security_hub_aws_redshift_cluster_elastic_ip_status import SecurityHubAwsRedshiftClusterElasticIpStatus
from .security_hub_aws_redshift_cluster_endpoint import SecurityHubAwsRedshiftClusterEndpoint
from .security_hub_aws_redshift_cluster_hsm_status import SecurityHubAwsRedshiftClusterHsmStatus
from .security_hub_aws_redshift_cluster_iam_role import SecurityHubAwsRedshiftClusterIamRole
from .security_hub_aws_redshift_cluster_logging_status import SecurityHubAwsRedshiftClusterLoggingStatus
from .security_hub_aws_redshift_cluster_pending_modified_values import SecurityHubAwsRedshiftClusterPendingModifiedValues
from .security_hub_aws_redshift_cluster_resize_info import SecurityHubAwsRedshiftClusterResizeInfo
from .security_hub_aws_redshift_cluster_restore_status import SecurityHubAwsRedshiftClusterRestoreStatus
from .security_hub_aws_redshift_cluster_vpc_security_group import SecurityHubAwsRedshiftClusterVpcSecurityGroup


class SecurityHubAwsRedshiftClusterDetails(BaseModel):
    AllowVersionUpgrade: StrictBool | None = None
    AutomatedSnapshotRetentionPeriod: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    ClusterAvailabilityStatus: StrictStr | None = None
    ClusterCreateTime: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    ClusterNodes: list[SecurityHubAwsRedshiftClusterClusterNode] | None = None
    ClusterParameterGroups: list[SecurityHubAwsRedshiftClusterClusterParameterGroup] | None = None
    ClusterPublicKey: StrictStr | None = None
    ClusterRevisionNumber: StrictStr | None = None
    ClusterSecurityGroups: list[SecurityHubAwsRedshiftClusterClusterSecurityGroup] | None = None
    ClusterSnapshotCopyStatus: SecurityHubAwsRedshiftClusterClusterSnapshotCopyStatus | None = None
    ClusterStatus: StrictStr | None = None
    ClusterSubnetGroupName: StrictStr | None = None
    ClusterVersion: StrictStr | None = None
    DBName: StrictStr | None = None
    DeferredMaintenanceWindows: list[SecurityHubAwsRedshiftClusterDeferredMaintenanceWindow] | None = None
    ElasticIpStatus: SecurityHubAwsRedshiftClusterElasticIpStatus | None = None
    ElasticResizeNumberOfNodeOptions: StrictStr | None = None
    Encrypted: StrictBool | None = None
    Endpoint: SecurityHubAwsRedshiftClusterEndpoint | None = None
    EnhancedVpcRouting: StrictBool | None = None
    ExpectedNextSnapshotScheduleTime: StrictStr | None = None
    ExpectedNextSnapshotScheduleTimeStatus: StrictStr | None = None
    HsmStatus: SecurityHubAwsRedshiftClusterHsmStatus | None = None
    IamRoles: list[SecurityHubAwsRedshiftClusterIamRole] | None = None
    KmsKeyId: StrictStr | None = None
    MaintenanceTrackName: StrictStr | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    NextMaintenanceWindowStartTime: StrictStr | None = None
    NodeType: StrictStr | None = None
    NumberOfNodes: StrictInt | None = None
    PendingActions: list[StrictStr] | None = None
    PendingModifiedValues: SecurityHubAwsRedshiftClusterPendingModifiedValues | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    ResizeInfo: SecurityHubAwsRedshiftClusterResizeInfo | None = None
    RestoreStatus: SecurityHubAwsRedshiftClusterRestoreStatus | None = None
    SnapshotScheduleIdentifier: StrictStr | None = None
    SnapshotScheduleState: StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcSecurityGroups: list[SecurityHubAwsRedshiftClusterVpcSecurityGroup] | None = None
    LoggingStatus: SecurityHubAwsRedshiftClusterLoggingStatus | None = None
