from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_volume_detail import GuardDutyVolumeDetail


class GuardDutyEbsVolumeDetails(BaseModel):
    ScannedVolumeDetails: list[GuardDutyVolumeDetail] | None = None
    SkippedVolumeDetails: list[GuardDutyVolumeDetail] | None = None
