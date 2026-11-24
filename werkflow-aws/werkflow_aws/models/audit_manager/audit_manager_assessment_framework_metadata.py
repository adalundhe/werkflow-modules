from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerAssessmentFrameworkMetadata(BaseModel):
    arn: StrictStr | None = None
    id: StrictStr | None = None
    type: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    logo: StrictStr | None = None
    complianceType: StrictStr | None = None
    controlsCount: StrictInt | None = None
    controlSetsCount: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
