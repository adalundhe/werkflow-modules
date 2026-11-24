from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_db_instance_status_info import NeptuneDBInstanceStatusInfo
from .neptune_db_parameter_group_status import NeptuneDBParameterGroupStatus
from .neptune_db_security_group_membership import NeptuneDBSecurityGroupMembership
from .neptune_db_subnet_group import NeptuneDBSubnetGroup
from .neptune_domain_membership import NeptuneDomainMembership
from .neptune_endpoint import NeptuneEndpoint
from .neptune_option_group_membership import NeptuneOptionGroupMembership
from .neptune_pending_modified_values import NeptunePendingModifiedValues
from .neptune_vpc_security_group_membership import NeptuneVpcSecurityGroupMembership


class NeptuneDBInstance(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    Engine: StrictStr | None = None
    DBInstanceStatus: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    DBName: StrictStr | None = None
    Endpoint: NeptuneEndpoint | None = None
    AllocatedStorage: StrictInt | None = None
    InstanceCreateTime: datetime.datetime | StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    DBSecurityGroups: list[NeptuneDBSecurityGroupMembership] | None = None
    VpcSecurityGroups: list[NeptuneVpcSecurityGroupMembership] | None = None
    DBParameterGroups: list[NeptuneDBParameterGroupStatus] | None = None
    AvailabilityZone: StrictStr | None = None
    DBSubnetGroup: NeptuneDBSubnetGroup | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    PendingModifiedValues: NeptunePendingModifiedValues | None = None
    LatestRestorableTime: datetime.datetime | StrictStr | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    ReadReplicaSourceDBInstanceIdentifier: StrictStr | None = None
    ReadReplicaDBInstanceIdentifiers: list[StrictStr] | None = None
    ReadReplicaDBClusterIdentifiers: list[StrictStr] | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    OptionGroupMemberships: list[NeptuneOptionGroupMembership] | None = None
    CharacterSetName: StrictStr | None = None
    SecondaryAvailabilityZone: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    StatusInfos: list[NeptuneDBInstanceStatusInfo] | None = None
    StorageType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    DbInstancePort: StrictInt | None = None
    DBClusterIdentifier: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    DomainMemberships: list[NeptuneDomainMembership] | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    EnhancedMonitoringResourceArn: StrictStr | None = None
    MonitoringRoleArn: StrictStr | None = None
    PromotionTier: StrictInt | None = None
    DBInstanceArn: StrictStr | None = None
    Timezone: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    PerformanceInsightsEnabled: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    EnabledCloudwatchLogsExports: list[StrictStr] | None = None
    DeletionProtection: StrictBool | None = None
    NetworkType: StrictStr | None = None
