from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_ebs_volumes_result import GuardDutyEbsVolumesResult


class GuardDutyScanEc2InstanceWithFindingsResult(BaseModel):
    EbsVolumes: GuardDutyEbsVolumesResult | None = None
