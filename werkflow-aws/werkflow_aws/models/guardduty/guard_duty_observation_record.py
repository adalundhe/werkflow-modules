from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_account_overview import GuardDutyAccountOverview
from .guard_duty_detection_coverage import GuardDutyDetectionCoverage
from .guard_duty_distribution import GuardDutyDistribution
from .guard_duty_finding_detail import GuardDutyFindingDetail
from .guard_duty_investigation_indicator import GuardDutyInvestigationIndicator
from .guard_duty_investigation_malware_scan import GuardDutyInvestigationMalwareScan
from .guard_duty_investigation_resource import GuardDutyInvestigationResource
from .guard_duty_kubernetes_activity import GuardDutyKubernetesActivity
from .guard_duty_network_activity import GuardDutyNetworkActivity
from .guard_duty_rds_login_activity import GuardDutyRdsLoginActivity
from .guard_duty_recommendation import GuardDutyRecommendation
from .guard_duty_related_findings import GuardDutyRelatedFindings
from .guard_duty_representative_finding import GuardDutyRepresentativeFinding
from .guard_duty_runtime_signals import GuardDutyRuntimeSignals
from .guard_duty_s3_activity import GuardDutyS3Activity


class GuardDutyObservationRecord(BaseModel):
    ObservationType: StrictStr | None = None
    FindingDetail: GuardDutyFindingDetail | None = None
    Resource: GuardDutyInvestigationResource | None = None
    NetworkActivity: GuardDutyNetworkActivity | None = None
    RdsLoginActivity: GuardDutyRdsLoginActivity | None = None
    S3Activity: GuardDutyS3Activity | None = None
    KubernetesActivity: GuardDutyKubernetesActivity | None = None
    MalwareScan: GuardDutyInvestigationMalwareScan | None = None
    RelatedFindings: GuardDutyRelatedFindings | None = None
    DetectionCoverage: GuardDutyDetectionCoverage | None = None
    AccountOverview: GuardDutyAccountOverview | None = None
    Recommendations: list[GuardDutyRecommendation] | None = None
    RuntimeSignals: GuardDutyRuntimeSignals | None = None
    Distribution: GuardDutyDistribution | None = None
    RepresentativeResources: list[GuardDutyRepresentativeFinding] | None = None
    Indicators: list[GuardDutyInvestigationIndicator] | None = None
