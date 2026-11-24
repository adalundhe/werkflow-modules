from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AuditManagerDelegationMetadata(BaseModel):
    id: StrictStr | None = None
    assessmentName: StrictStr | None = None
    assessmentId: StrictStr | None = None
    status: StrictStr | None = None
    roleArn: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    controlSetName: StrictStr | None = None
