from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class BackupStartScanJobRequest(BaseModel):
    BackupVaultName: StrictStr
    IamRoleArn: StrictStr
    MalwareScanner: Literal['GUARDDUTY']
    RecoveryPointArn: StrictStr
    ScanMode: Literal['FULL_SCAN', 'INCREMENTAL_SCAN']
    ScannerRoleArn: StrictStr
    ContinuousScanEndTime: datetime.datetime | StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
    ScanBaseRecoveryPointArn: StrictStr | None = None
