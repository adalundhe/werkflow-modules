from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_continuous_scan_details import GuardDutyContinuousScanDetails


class GuardDutyRecoveryPoint(BaseModel):
    BackupVaultName: StrictStr
    ContinuousScanDetails: GuardDutyContinuousScanDetails | None = None
