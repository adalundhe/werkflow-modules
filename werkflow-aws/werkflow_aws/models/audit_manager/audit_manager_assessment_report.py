from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AuditManagerAssessmentReport(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    awsAccountId: StrictStr | None = None
    assessmentId: StrictStr | None = None
    assessmentName: StrictStr | None = None
    author: StrictStr | None = None
    status: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
