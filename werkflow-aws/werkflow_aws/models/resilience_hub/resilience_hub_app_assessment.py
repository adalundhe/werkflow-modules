from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .resilience_hub_assessment_summary import ResilienceHubAssessmentSummary
from .resilience_hub_cost import ResilienceHubCost
from .resilience_hub_disruption_compliance import ResilienceHubDisruptionCompliance
from .resilience_hub_resiliency_policy import ResilienceHubResiliencyPolicy
from .resilience_hub_resiliency_score import ResilienceHubResiliencyScore
from .resilience_hub_resource_errors_details import ResilienceHubResourceErrorsDetails


class ResilienceHubAppAssessment(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    assessmentArn: StrictStr | None = None
    assessmentName: StrictStr | None = None
    assessmentStatus: StrictStr | None = None
    compliance: dict[StrictStr, ResilienceHubDisruptionCompliance] | None = None
    complianceStatus: StrictStr | None = None
    cost: ResilienceHubCost | None = None
    driftStatus: StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    invoker: StrictStr | None = None
    message: StrictStr | None = None
    policy: ResilienceHubResiliencyPolicy | None = None
    resiliencyScore: ResilienceHubResiliencyScore | None = None
    resourceErrorsDetails: ResilienceHubResourceErrorsDetails | None = None
    startTime: datetime.datetime | StrictStr | None = None
    summary: ResilienceHubAssessmentSummary | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    versionName: StrictStr | None = None
