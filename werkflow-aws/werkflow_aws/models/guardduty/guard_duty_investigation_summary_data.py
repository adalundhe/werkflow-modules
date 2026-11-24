from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_account_analysis import GuardDutyAccountAnalysis
from .guard_duty_countermeasure import GuardDutyCountermeasure
from .guard_duty_key_observations import GuardDutyKeyObservations
from .guard_duty_organization_analysis import GuardDutyOrganizationAnalysis
from .guard_duty_recommendation import GuardDutyRecommendation
from .guard_duty_threat_assessment import GuardDutyThreatAssessment


class GuardDutyInvestigationSummaryData(BaseModel):
    FindingType: StrictStr | None = None
    ThreatAssessment: GuardDutyThreatAssessment | None = None
    Countermeasures: list[GuardDutyCountermeasure] | None = None
    AccountAnalysis: GuardDutyAccountAnalysis | None = None
    OrganizationAnalysis: GuardDutyOrganizationAnalysis | None = None
    KeyObservations: GuardDutyKeyObservations | None = None
    Recommendations: list[GuardDutyRecommendation] | None = None
