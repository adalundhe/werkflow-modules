from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_rds_db_domain_membership import SecurityHubAwsRdsDbDomainMembership
from .security_hub_aws_rds_db_instance_associated_role import SecurityHubAwsRdsDbInstanceAssociatedRole
from .security_hub_aws_rds_db_instance_endpoint import SecurityHubAwsRdsDbInstanceEndpoint
from .security_hub_aws_rds_db_instance_vpc_security_group import SecurityHubAwsRdsDbInstanceVpcSecurityGroup
from .security_hub_aws_rds_db_option_group_membership import SecurityHubAwsRdsDbOptionGroupMembership
from .security_hub_aws_rds_db_parameter_group import SecurityHubAwsRdsDbParameterGroup
from .security_hub_aws_rds_db_pending_modified_values import SecurityHubAwsRdsDbPendingModifiedValues
from .security_hub_aws_rds_db_processor_feature import SecurityHubAwsRdsDbProcessorFeature
from .security_hub_aws_rds_db_status_info import SecurityHubAwsRdsDbStatusInfo
from .security_hub_aws_rds_db_subnet_group import SecurityHubAwsRdsDbSubnetGroup


class SecurityHubAwsRdsDbInstanceDetails(BaseModel):
    AssociatedRoles: list[SecurityHubAwsRdsDbInstanceAssociatedRole] | None = None
    CACertificateIdentifier: StrictStr | None = None
    DBClusterIdentifier: StrictStr | None = None
    DBInstanceIdentifier: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    DbInstancePort: StrictInt | None = None
    DbiResourceId: StrictStr | None = None
    DBName: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    Endpoint: SecurityHubAwsRdsDbInstanceEndpoint | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    InstanceCreateTime: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    StorageEncrypted: StrictBool | None = None
    TdeCredentialArn: StrictStr | None = None
    VpcSecurityGroups: list[SecurityHubAwsRdsDbInstanceVpcSecurityGroup] | None = None
    MultiAz: StrictBool | None = None
    EnhancedMonitoringResourceArn: StrictStr | None = None
    DbInstanceStatus: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    DbSecurityGroups: list[StrictStr] | None = None
    DbParameterGroups: list[SecurityHubAwsRdsDbParameterGroup] | None = None
    AvailabilityZone: StrictStr | None = None
    DbSubnetGroup: SecurityHubAwsRdsDbSubnetGroup | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    PendingModifiedValues: SecurityHubAwsRdsDbPendingModifiedValues | None = None
    LatestRestorableTime: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    ReadReplicaSourceDBInstanceIdentifier: StrictStr | None = None
    ReadReplicaDBInstanceIdentifiers: list[StrictStr] | None = None
    ReadReplicaDBClusterIdentifiers: list[StrictStr] | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    OptionGroupMemberships: list[SecurityHubAwsRdsDbOptionGroupMembership] | None = None
    CharacterSetName: StrictStr | None = None
    SecondaryAvailabilityZone: StrictStr | None = None
    StatusInfos: list[SecurityHubAwsRdsDbStatusInfo] | None = None
    StorageType: StrictStr | None = None
    DomainMemberships: list[SecurityHubAwsRdsDbDomainMembership] | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    PromotionTier: StrictInt | None = None
    Timezone: StrictStr | None = None
    PerformanceInsightsEnabled: StrictBool | None = None
    PerformanceInsightsKmsKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    EnabledCloudWatchLogsExports: list[StrictStr] | None = None
    ProcessorFeatures: list[SecurityHubAwsRdsDbProcessorFeature] | None = None
    ListenerEndpoint: SecurityHubAwsRdsDbInstanceEndpoint | None = None
    MaxAllocatedStorage: StrictInt | None = None
