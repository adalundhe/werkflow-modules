from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerAssessmentFrameworkShareRequest(BaseModel):
    id: StrictStr | None = None
    frameworkId: StrictStr | None = None
    frameworkName: StrictStr | None = None
    frameworkDescription: StrictStr | None = None
    status: StrictStr | None = None
    sourceAccount: StrictStr | None = None
    destinationAccount: StrictStr | None = None
    destinationRegion: StrictStr | None = None
    expirationTime: datetime.datetime | StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None
    comment: StrictStr | None = None
    standardControlsCount: StrictInt | None = None
    customControlsCount: StrictInt | None = None
    complianceType: StrictStr | None = None
