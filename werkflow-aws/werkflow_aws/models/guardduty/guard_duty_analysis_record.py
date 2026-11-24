from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_investigation_account_analysis import GuardDutyInvestigationAccountAnalysis
from .guard_duty_investigation_indicator import GuardDutyInvestigationIndicator
from .guard_duty_investigation_threat_assessment import GuardDutyInvestigationThreatAssessment
from .guard_duty_kubernetes_policy_violation import GuardDutyKubernetesPolicyViolation
from .guard_duty_process import GuardDutyProcess
from .guard_duty_s3_analysis import GuardDutyS3Analysis


class GuardDutyAnalysisRecord(BaseModel):
    AnalysisType: StrictStr | None = None
    ThreatAssessment: GuardDutyInvestigationThreatAssessment | None = None
    KubernetesPolicyViolation: GuardDutyKubernetesPolicyViolation | None = None
    S3Analysis: GuardDutyS3Analysis | None = None
    Processes: list[GuardDutyProcess] | None = None
    AccountAnalysis: GuardDutyInvestigationAccountAnalysis | None = None
    Indicators: list[GuardDutyInvestigationIndicator] | None = None
