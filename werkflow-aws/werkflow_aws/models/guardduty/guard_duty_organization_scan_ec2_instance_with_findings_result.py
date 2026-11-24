from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_organization_ebs_volumes_result import GuardDutyOrganizationEbsVolumesResult


class GuardDutyOrganizationScanEc2InstanceWithFindingsResult(BaseModel):
    EbsVolumes: GuardDutyOrganizationEbsVolumesResult | None = None
