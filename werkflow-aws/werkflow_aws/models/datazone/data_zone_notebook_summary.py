from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneNotebookSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    domainId: StrictStr | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
