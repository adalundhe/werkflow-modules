from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AuditManagerDelegation(BaseModel):
    id: StrictStr | None = None
    assessmentName: StrictStr | None = None
    assessmentId: StrictStr | None = None
    status: StrictStr | None = None
    roleArn: StrictStr | None = None
    roleType: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None
    controlSetId: StrictStr | None = None
    comment: StrictStr | None = None
    createdBy: StrictStr | None = None
