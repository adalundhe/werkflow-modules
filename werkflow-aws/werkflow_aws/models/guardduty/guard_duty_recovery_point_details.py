from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_scan_configuration_continuous_scan_details import GuardDutyScanConfigurationContinuousScanDetails


class GuardDutyRecoveryPointDetails(BaseModel):
    RecoveryPointArn: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    ContinuousScanDetails: GuardDutyScanConfigurationContinuousScanDetails | None = None
