from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .resilience_hub_cost import ResilienceHubCost


class ResilienceHubAppAssessmentSummary(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    assessmentArn: StrictStr | None = None
    assessmentName: StrictStr | None = None
    assessmentStatus: StrictStr | None = None
    complianceStatus: StrictStr | None = None
    cost: ResilienceHubCost | None = None
    driftStatus: StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    invoker: StrictStr | None = None
    message: StrictStr | None = None
    resiliencyScore: StrictFloat | StrictInt | None = None
    startTime: datetime.datetime | StrictStr | None = None
    versionName: StrictStr | None = None
