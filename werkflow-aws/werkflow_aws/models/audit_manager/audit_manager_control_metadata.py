from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AuditManagerControlMetadata(BaseModel):
    arn: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    controlSources: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
