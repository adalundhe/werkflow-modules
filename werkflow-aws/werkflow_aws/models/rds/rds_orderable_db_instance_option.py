from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .rds_availability_zone_model import RDSAvailabilityZoneModel
from .rds_available_additional_storage_volumes_option import RDSAvailableAdditionalStorageVolumesOption
from .rds_available_processor_feature import RDSAvailableProcessorFeature


class RDSOrderableDBInstanceOption(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    AvailabilityZoneGroup: StrictStr | None = None
    AvailabilityZones: list[RDSAvailabilityZoneModel] | None = None
    MultiAZCapable: StrictBool | None = None
    ReadReplicaCapable: StrictBool | None = None
    Vpc: StrictBool | None = None
    SupportsStorageEncryption: StrictBool | None = None
    StorageType: StrictStr | None = None
    SupportsIops: StrictBool | None = None
    SupportsStorageThroughput: StrictBool | None = None
    SupportsEnhancedMonitoring: StrictBool | None = None
    SupportsIAMDatabaseAuthentication: StrictBool | None = None
    SupportsPerformanceInsights: StrictBool | None = None
    MinStorageSize: StrictInt | None = None
    MaxStorageSize: StrictInt | None = None
    MinIopsPerDbInstance: StrictInt | None = None
    MaxIopsPerDbInstance: StrictInt | None = None
    MinIopsPerGib: StrictFloat | StrictInt | None = None
    MaxIopsPerGib: StrictFloat | StrictInt | None = None
    MinStorageThroughputPerDbInstance: StrictInt | None = None
    MaxStorageThroughputPerDbInstance: StrictInt | None = None
    MinStorageThroughputPerIops: StrictFloat | StrictInt | None = None
    MaxStorageThroughputPerIops: StrictFloat | StrictInt | None = None
    AvailableProcessorFeatures: list[RDSAvailableProcessorFeature] | None = None
    SupportedEngineModes: list[StrictStr] | None = None
    SupportsStorageAutoscaling: StrictBool | None = None
    SupportsKerberosAuthentication: StrictBool | None = None
    OutpostCapable: StrictBool | None = None
    SupportedActivityStreamModes: list[StrictStr] | None = None
    SupportsGlobalDatabases: StrictBool | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
    SupportsClusters: StrictBool | None = None
    SupportsDedicatedLogVolume: StrictBool | None = None
    SupportsAdditionalStorageVolumes: StrictBool | None = None
    SupportsHttpEndpoint: StrictBool | None = None
    AvailableAdditionalStorageVolumesOptions: list[RDSAvailableAdditionalStorageVolumesOption] | None = None
