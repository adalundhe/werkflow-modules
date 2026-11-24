from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ResilienceHubAppSummary(BaseModel):
    appArn: StrictStr | None = None
    assessmentSchedule: StrictStr | None = None
    awsApplicationArn: StrictStr | None = None
    complianceStatus: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    driftStatus: StrictStr | None = None
    lastAppComplianceEvaluationTime: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    resiliencyScore: StrictFloat | StrictInt | None = None
    rpoInSecs: StrictInt | None = None
    rtoInSecs: StrictInt | None = None
    status: StrictStr | None = None
