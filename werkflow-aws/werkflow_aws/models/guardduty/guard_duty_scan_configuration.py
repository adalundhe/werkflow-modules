from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_incremental_scan_details import GuardDutyIncrementalScanDetails
from .guard_duty_scan_configuration_recovery_point import GuardDutyScanConfigurationRecoveryPoint
from .guard_duty_trigger_details import GuardDutyTriggerDetails


class GuardDutyScanConfiguration(BaseModel):
    Role: StrictStr | None = None
    TriggerDetails: GuardDutyTriggerDetails | None = None
    IncrementalScanDetails: GuardDutyIncrementalScanDetails | None = None
    RecoveryPoint: GuardDutyScanConfigurationRecoveryPoint | None = None
