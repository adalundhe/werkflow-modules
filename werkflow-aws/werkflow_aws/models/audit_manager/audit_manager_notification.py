from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AuditManagerNotification(BaseModel):
    id: StrictStr | None = None
    assessmentId: StrictStr | None = None
    assessmentName: StrictStr | None = None
    controlSetId: StrictStr | None = None
    controlSetName: StrictStr | None = None
    description: StrictStr | None = None
    eventTime: datetime.datetime | StrictStr | None = None
    source: StrictStr | None = None
