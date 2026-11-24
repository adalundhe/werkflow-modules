from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_resource_details import GuardDutyResourceDetails
from .guard_duty_scan_result_details import GuardDutyScanResultDetails
from .guard_duty_trigger_details import GuardDutyTriggerDetails
from .guard_duty_volume_detail import GuardDutyVolumeDetail


class GuardDutyScan(BaseModel):
    DetectorId: StrictStr | None = None
    AdminDetectorId: StrictStr | None = None
    ScanId: StrictStr | None = None
    ScanStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ScanStartTime: datetime.datetime | StrictStr | None = None
    ScanEndTime: datetime.datetime | StrictStr | None = None
    TriggerDetails: GuardDutyTriggerDetails | None = None
    ResourceDetails: GuardDutyResourceDetails | None = None
    ScanResultDetails: GuardDutyScanResultDetails | None = None
    AccountId: StrictStr | None = None
    TotalBytes: StrictInt | None = None
    FileCount: StrictInt | None = None
    AttachedVolumes: list[GuardDutyVolumeDetail] | None = None
    ScanType: StrictStr | None = None
