from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume_model import RDSAdditionalStorageVolumeModel
from .rds_pending_cloudwatch_logs_exports_model import RDSPendingCloudwatchLogsExportsModel
from .rds_processor_feature_model import RDSProcessorFeatureModel


class RDSPendingModifiedValuesModel(BaseModel):
    DBInstanceClass: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    MasterUserPassword: StrictStr | None = None
    Port: StrictInt | None = None
    BackupRetentionPeriod: StrictInt | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    DBInstanceIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    DBSubnetGroupName: StrictStr | None = None
    PendingCloudwatchLogsExports: RDSPendingCloudwatchLogsExportsModel | None = None
    ProcessorFeatures: list[RDSProcessorFeatureModel] | None = None
    AutomationMode: StrictStr | None = None
    ResumeFullAutomationModeTime: datetime.datetime | StrictStr | None = None
    MultiTenant: StrictBool | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    DedicatedLogVolume: StrictBool | None = None
    Engine: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolumeModel] | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
