from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_account_affected_resource import GuardDutyAccountAffectedResource
from .guard_duty_findings_summary import GuardDutyFindingsSummary
from .guard_duty_tactic_coverage import GuardDutyTacticCoverage


class GuardDutyAccountAnalysis(BaseModel):
    FindingsSummary: GuardDutyFindingsSummary | None = None
    TacticCoverage: list[GuardDutyTacticCoverage] | None = None
    AffectedResources: list[GuardDutyAccountAffectedResource] | None = None
