from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneDataProductRevision(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    revision: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
