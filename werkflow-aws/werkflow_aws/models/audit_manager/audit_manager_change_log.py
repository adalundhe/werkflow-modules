from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AuditManagerChangeLog(BaseModel):
    objectType: StrictStr | None = None
    objectName: StrictStr | None = None
    action: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
