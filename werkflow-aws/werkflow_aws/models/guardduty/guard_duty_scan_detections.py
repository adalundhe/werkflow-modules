from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_highest_severity_threat_details import GuardDutyHighestSeverityThreatDetails
from .guard_duty_scanned_item_count import GuardDutyScannedItemCount
from .guard_duty_threat_detected_by_name import GuardDutyThreatDetectedByName
from .guard_duty_threats_detected_item_count import GuardDutyThreatsDetectedItemCount


class GuardDutyScanDetections(BaseModel):
    ScannedItemCount: GuardDutyScannedItemCount | None = None
    ThreatsDetectedItemCount: GuardDutyThreatsDetectedItemCount | None = None
    HighestSeverityThreatDetails: GuardDutyHighestSeverityThreatDetails | None = None
    ThreatDetectedByName: GuardDutyThreatDetectedByName | None = None
