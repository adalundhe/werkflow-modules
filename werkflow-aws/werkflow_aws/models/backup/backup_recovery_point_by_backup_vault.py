from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .backup_aggregated_scan_result import BackupAggregatedScanResult
from .backup_calculated_lifecycle import BackupCalculatedLifecycle
from .backup_lifecycle import BackupLifecycle
from .backup_recovery_point_creator import BackupRecoveryPointCreator


class BackupRecoveryPointByBackupVault(BaseModel):
    RecoveryPointArn: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    SourceBackupVaultArn: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    CreatedBy: BackupRecoveryPointCreator | None = None
    IamRoleArn: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    InitiationDate: datetime.datetime | StrictStr | None = None
    CompletionDate: datetime.datetime | StrictStr | None = None
    BackupSizeInBytes: StrictInt | None = None
    CalculatedLifecycle: BackupCalculatedLifecycle | None = None
    Lifecycle: BackupLifecycle | None = None
    EncryptionKeyArn: StrictStr | None = None
    IsEncrypted: StrictBool | None = None
    LastRestoreTime: datetime.datetime | StrictStr | None = None
    ParentRecoveryPointArn: StrictStr | None = None
    CompositeMemberIdentifier: StrictStr | None = None
    IsParent: StrictBool | None = None
    ResourceName: StrictStr | None = None
    VaultType: StrictStr | None = None
    IndexStatus: StrictStr | None = None
    IndexStatusMessage: StrictStr | None = None
    EncryptionKeyType: StrictStr | None = None
    AggregatedScanResult: BackupAggregatedScanResult | None = None
