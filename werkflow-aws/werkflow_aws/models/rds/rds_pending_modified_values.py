from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume import RDSAdditionalStorageVolume
from .rds_automation_mode import RDSAutomationMode
from .rds_pending_cloudwatch_logs_exports import RDSPendingCloudwatchLogsExports
from .rds_processor_feature import RDSProcessorFeature


class RDSPendingModifiedValues(BaseModel):
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
    PendingCloudwatchLogsExports: RDSPendingCloudwatchLogsExports | None = None
    ProcessorFeatures: list[RDSProcessorFeature] | None = None
    AutomationMode: RDSAutomationMode | None = None
    ResumeFullAutomationModeTime: datetime.datetime | None = None
    MultiTenant: StrictBool | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    DedicatedLogVolume: StrictBool | None = None
    Engine: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolume] | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
