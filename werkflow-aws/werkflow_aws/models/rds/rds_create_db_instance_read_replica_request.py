from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume_model import RDSAdditionalStorageVolumeModel
from .rds_processor_feature_model import RDSProcessorFeatureModel
from .rds_tag_model import RDSTagModel
from .rds_tag_specification_model import RDSTagSpecificationModel


class RDSCreateDBInstanceReadReplicaRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    SourceDBInstanceIdentifier: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Port: StrictInt | None = None
    MultiAZ: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    DBParameterGroupName: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    Tags: list[RDSTagModel] | None = None
    DBSubnetGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    StorageType: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    DatabaseInsightsMode: Literal['standard', 'advanced'] | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    ProcessorFeatures: list[RDSProcessorFeatureModel] | None = None
    UseDefaultProcessorFeatures: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    Domain: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    DomainFqdn: StrictStr | None = None
    DomainOu: StrictStr | None = None
    DomainAuthSecretArn: StrictStr | None = None
    DomainDnsIps: list[StrictStr] | None = None
    ReplicaMode: Literal['open-read-only', 'mounted'] | None = None
    EnableCustomerOwnedIp: StrictBool | None = None
    NetworkType: StrictStr | None = None
    MaxAllocatedStorage: StrictInt | None = None
    BackupTarget: StrictStr | None = None
    CustomIamInstanceProfile: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    SourceDBClusterIdentifier: StrictStr | None = None
    DedicatedLogVolume: StrictBool | None = None
    UpgradeStorageConfig: StrictBool | None = None
    CACertificateIdentifier: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolumeModel] | None = None
    TagSpecifications: list[RDSTagSpecificationModel] | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
    SourceRegion: StrictStr | None = None
