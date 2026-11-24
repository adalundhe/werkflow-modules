from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .guard_duty_action import GuardDutyAction
from .guard_duty_detection import GuardDutyDetection
from .guard_duty_ebs_volume_scan_details import GuardDutyEbsVolumeScanDetails
from .guard_duty_evidence import GuardDutyEvidence
from .guard_duty_malware_scan_details import GuardDutyMalwareScanDetails
from .guard_duty_runtime_details import GuardDutyRuntimeDetails
from .guard_duty_service_additional_info import GuardDutyServiceAdditionalInfo


class GuardDutyService(BaseModel):
    Action: GuardDutyAction | None = None
    Evidence: GuardDutyEvidence | None = None
    Archived: StrictBool | None = None
    Count: StrictInt | None = None
    DetectorId: StrictStr | None = None
    EventFirstSeen: StrictStr | None = None
    EventLastSeen: StrictStr | None = None
    ResourceRole: StrictStr | None = None
    ServiceName: StrictStr | None = None
    UserFeedback: StrictStr | None = None
    AdditionalInfo: GuardDutyServiceAdditionalInfo | None = None
    FeatureName: StrictStr | None = None
    EbsVolumeScanDetails: GuardDutyEbsVolumeScanDetails | None = None
    RuntimeDetails: GuardDutyRuntimeDetails | None = None
    Detection: GuardDutyDetection | None = None
    MalwareScanDetails: GuardDutyMalwareScanDetails | None = None
