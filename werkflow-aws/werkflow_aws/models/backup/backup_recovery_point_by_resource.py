from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .backup_aggregated_scan_result import BackupAggregatedScanResult


class BackupRecoveryPointByResource(BaseModel):
    RecoveryPointArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    BackupSizeBytes: StrictInt | None = None
    BackupVaultName: StrictStr | None = None
    IsParent: StrictBool | None = None
    ParentRecoveryPointArn: StrictStr | None = None
    ResourceName: StrictStr | None = None
    VaultType: StrictStr | None = None
    IndexStatus: StrictStr | None = None
    IndexStatusMessage: StrictStr | None = None
    EncryptionKeyType: StrictStr | None = None
    AggregatedScanResult: BackupAggregatedScanResult | None = None
