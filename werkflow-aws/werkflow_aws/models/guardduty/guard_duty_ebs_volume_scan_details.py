from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_scan_detections import GuardDutyScanDetections


class GuardDutyEbsVolumeScanDetails(BaseModel):
    ScanId: StrictStr | None = None
    ScanStartedAt: datetime.datetime | StrictStr | None = None
    ScanCompletedAt: datetime.datetime | StrictStr | None = None
    TriggerFindingId: StrictStr | None = None
    Sources: list[StrictStr] | None = None
    ScanDetections: GuardDutyScanDetections | None = None
    ScanType: StrictStr | None = None
