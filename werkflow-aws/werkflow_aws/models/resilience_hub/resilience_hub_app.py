from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .resilience_hub_event_subscription import ResilienceHubEventSubscription
from .resilience_hub_permission_model import ResilienceHubPermissionModel


class ResilienceHubApp(BaseModel):
    appArn: StrictStr | None = None
    assessmentSchedule: StrictStr | None = None
    awsApplicationArn: StrictStr | None = None
    complianceStatus: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    driftStatus: StrictStr | None = None
    eventSubscriptions: list[ResilienceHubEventSubscription] | None = None
    lastAppComplianceEvaluationTime: datetime.datetime | StrictStr | None = None
    lastDriftEvaluationTime: datetime.datetime | StrictStr | None = None
    lastResiliencyScoreEvaluationTime: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    permissionModel: ResilienceHubPermissionModel | None = None
    policyArn: StrictStr | None = None
    resiliencyScore: StrictFloat | StrictInt | None = None
    rpoInSecs: StrictInt | None = None
    rtoInSecs: StrictInt | None = None
    status: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
