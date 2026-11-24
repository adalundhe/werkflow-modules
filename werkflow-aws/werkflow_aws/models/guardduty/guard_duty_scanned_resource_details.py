from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_ebs_snapshot import GuardDutyEbsSnapshot
from .guard_duty_volume_detail import GuardDutyVolumeDetail


class GuardDutyScannedResourceDetails(BaseModel):
    EbsVolume: GuardDutyVolumeDetail | None = None
    EbsSnapshot: GuardDutyEbsSnapshot | None = None
