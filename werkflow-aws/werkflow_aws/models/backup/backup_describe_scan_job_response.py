from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_scan_job_creator import BackupScanJobCreator
from .backup_scan_result_info import BackupScanResultInfo


class BackupDescribeScanJobResponse(BaseModel):
    AccountId: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    CompletionDate: datetime.datetime | StrictStr | None = None
    ContinuousScanEndTime: datetime.datetime | StrictStr | None = None
    ContinuousScanStartTime: datetime.datetime | StrictStr | None = None
    CreatedBy: BackupScanJobCreator | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    MalwareScanner: StrictStr | None = None
    RecoveryPointArn: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResourceName: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ScanBaseRecoveryPointArn: StrictStr | None = None
    ScanId: StrictStr | None = None
    ScanJobId: StrictStr | None = None
    ScanMode: StrictStr | None = None
    ScanResult: BackupScanResultInfo | None = None
    ScannerRoleArn: StrictStr | None = None
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
