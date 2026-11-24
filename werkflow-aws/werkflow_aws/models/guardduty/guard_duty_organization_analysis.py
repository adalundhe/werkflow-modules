from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_account_summary import GuardDutyAccountSummary
from .guard_duty_organization_findings_summary import GuardDutyOrganizationFindingsSummary


class GuardDutyOrganizationAnalysis(BaseModel):
    FindingsSummary: GuardDutyOrganizationFindingsSummary | None = None
    AccountBreakdown: list[GuardDutyAccountSummary] | None = None
