from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_organization_ebs_volumes import GuardDutyOrganizationEbsVolumes


class GuardDutyOrganizationScanEc2InstanceWithFindings(BaseModel):
    EbsVolumes: GuardDutyOrganizationEbsVolumes | None = None
